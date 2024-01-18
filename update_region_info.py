#!/usr/bin/env python3

import json, boto3
from datetime import datetime

# Load the region data, announces.json is manually updated
with open("announces.json") as f:
    data = json.load(f)

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

# Keep things organized
data.sort(key=lambda x: (x['appeared_ip_ranges'], x.get('announced', ''), x['region']))

with open("announces.json", "wt", encoding="utf-8", newline="") as f:
    json.dump(data, f, indent=4)
    f.write("\n")

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

        if 'announced' in cur and 'days_to_announce' in cur and 'announce_url' in cur:
            row.append("[" + cur['announced'] + "](" + cur['announce_url'] + ")")
            row.append(f"{cur['days_to_announce']:,}")
        else:
            row += ['', '']
        
        f.write('| ' + ' | '.join(row) + ' |\n')

print("Done, announces.md created")
