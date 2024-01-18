#!/usr/bin/env python3

import json, boto3, sys, subprocess
from datetime import datetime, timedelta
if sys.version_info >= (3, 11): from datetime import UTC
else: import datetime as datetime_fix; UTC=datetime_fix.timezone.utc

def load_announces():
    # Load the region data, announces.json is partially manually updated
    with open("announces.json") as f:
        data = json.load(f)
    return data

def save_announces(data):
    # Keep things organized
    data.sort(key=lambda x: (x['appeared_ip_ranges'], x.get('announced', ''), x['region']))

    with open("announces.json", "wt", encoding="utf-8", newline="") as f:
        json.dump(data, f, indent=4)
        f.write("\n")

def update_names():
    data = load_announces()
    # Load, and cache, the region names, along with updating the days_to_announce value if needed
    for cur in data:
        if "name" not in cur:
            try:
                client = boto3.client('ssm', region_name="us-east-1")
                response = client.get_parameter(
                    Name = f'/aws/service/global-infrastructure/regions/{cur["region"]}/longName'
                )
                region_name = response['Parameter']['Value']
                cur["name"] = region_name
                print(f"Found '{cur['region']}' -> '{region_name}'")
            except:
                print(f"Unable to find name for '{cur['region']}'")

        if ("appeared_ip_ranges" in cur) and ("announced" in cur):
            to_datetime = lambda x: datetime(int(x[:4]), int(x[5:7]), int(x[8:10]))
            appeared = to_datetime(cur["appeared_ip_ranges"])
            announced = to_datetime(cur["announced"])
            days = int((announced - appeared).total_seconds() / 86400)
            if "days_to_announce" not in cur or days != cur.get("days_to_announce", 0):
                cur["days_to_announce"] = days
                print(f"Update days_to_announce to {days} for {cur['region']}")

    save_announces(data)

def create_markdown():
    update_names()

    data = load_announces()

    # Create a pretty version of the data file
    with open("announces.md", "wt", newline="", encoding="utf-8") as f:
        f.write("# AWS Regions\n")
        f.write("\n")
        f.write("This file is generated from the [source data](announces.json), which ")
        f.write("is manually updated as new regions show up in ip-ranges.json, and when ")
        f.write("regions are publicly announced.")
        f.write("\n")
        f.write("| Region | Name | ip-ranges.json | Announced | Days |\n")
        f.write("| :--- | :--- | :--- | :--- | ---: |\n")
        for cur in data:
            row = []
            row.append(cur['region'])
            row.append(cur.get('name', ''))
            if 'commit' in cur:
                commit_id, line_no = cur['commit'].split(",")
                row.append(f"[{cur['appeared_ip_ranges']}](https://github.com/seligman/aws-ip-ranges/blob/{commit_id}/ip-ranges.json#L{line_no})")
            else:
                row.append(cur['appeared_ip_ranges'])

            if cur.get("historical", 0) == 1:
                row[-1] += "<sup>**</sup>"
            elif cur.get("historical", 0) == 2:
                row[-1] += "<sup>*</sup>"

            if 'announced' in cur and 'days_to_announce' in cur and 'announce_url' in cur:
                row.append("[" + cur['announced'] + "](" + cur['announce_url'] + ")")
                row.append(f"{cur['days_to_announce']:,}")
            else:
                row += ['', '']
            
            f.write('| ' + ' | '.join(row) + ' |\n')
        
        f.write("\n")
        f.write("\\* = This region's date found in ip-ranges.json comes from a historical\n")
        f.write("view of the data before this repository was up and running.  It is likely\n")
        f.write("off by a few days.\n")
        f.write("\n")
        f.write("\\*\\* = This entry predates the historical view of data, the actual date is\n")
        f.write("sometime before the historical view of the data, which started on 2015-11-03.\n")

    print("Done, announces.md created")

def get_lines(cmd):
    cmd = cmd.split(' ')
    data = subprocess.check_output(cmd)
    data = data.decode("utf-8")
    data = data.split("\n")
    data = [x for x in data if len(x)]
    return data

def find_regions():
    bail = (datetime.now(UTC) - timedelta(days=90)).strftime("%Y-%m-%d")
    firsts = {}
    final_at = None

    print("Searching commits...", end="", flush=True)
    todo = get_lines("git log --all --pretty=format:%H,%cs")
    for i, row in enumerate(todo):
        print(f"\rSearching commits ({i})...", end="", flush=True)

        commit_id, at = row.split(",")
        if at <= bail:
            break
        for file_row in get_lines(f"git ls-tree -r --full-tree {commit_id} --format %(objectname),%(path)"):
            object_id, filename = file_row.split(",", 1)
            if filename == "ip-ranges.json":
                data = subprocess.check_output(f"git cat-file -p {object_id}".split(" "))
                data = data.decode("utf-8")
                parsed = json.loads(data)
                at = parsed["createDate"]
                final_at = at
                regions = set(x['region'] for x in parsed['prefixes']) | set(x['region'] for x in parsed['ipv6_prefixes'])
                for region in regions:
                    if region not in firsts or firsts[region]['at'] >= at:
                        firsts[region] = {
                            "at": at,
                            "object_id": object_id,
                            "commit_id": commit_id,
                        }

    print("", flush=True)

    announces = load_announces()

    for region, info in firsts.items():
        if info["at"] != final_at:
            print("Found region:")
            lines = subprocess.check_output(f"git cat-file -p {info['object_id']}".split(" "))
            lines = lines.decode("utf-8")
            line_no = None
            for i, row in enumerate(lines.split("\n")):
                if region in row:
                    line_no = i + 1
                    break
            to_add = {
                "region": region,
                "appeared_ip_ranges": info["at"][:10],
                "commit": f'{info["commit_id"]},{line_no}',
            }
            print(json.dumps(to_add, indent=4))
            found = False
            for cur in announces:
                if cur["region"] == region:
                    found = True
                    break
            if found:
                print("Already in announces.md")
            else:
                announces.append(to_add)
                print("Added to announces.md")
    
    save_announces(announces)

def main():
    cmds = [
        ("update", "Update markdown file", create_markdown),
        ("find", "Find recently added regions", find_regions),
    ]
    show_help = True
    for cmd, desc, func in cmds:
        if len(sys.argv) == 2 and sys.argv[1] == cmd:
            show_help = False
            func()
            break
    if show_help:
        print("Usage:")
        for cmd, desc, func in cmds:
            print(f"  {cmd} = {desc}")
        exit(1)

if __name__ == "__main__":
    main()
