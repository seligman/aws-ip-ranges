#!/usr/bin/env python3

import json, boto3
from datetime import datetime

# Load the region data, announces.json is manually updated
with open("announces.json") as f:
    data = json.load(f)

# Load, and cache, the region names, along with updating the days_to_announce value if needed
changed = False
for cur in data:
    if "name" not in cur:
        try:
            client = boto3.client('ssm', region_name="us-east-1")
            response = client.get_parameter(
                Name = f'/aws/service/global-infrastructure/regions/{cur["region"]}/longName'
            )
            region_name = response['Parameter']['Value']
            cur["name"] = region_name
            changed = True
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
            changed = True
            print(f"Update days_to_announce to {days} for {cur['region']}")

if changed:
    # If we found a new name, go ahead and cache it
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
        row = [
            cur['region'], 
            cur.get('name', ''),
            cur['appeared_ip_ranges'],
        ]
        if 'announced' in cur and 'days_to_announce' in cur and 'announce_url' in cur:
            row.append("[" + cur['announced'] + "](" + cur['announce_url'] + ")")
            row.append(f"{cur['days_to_announce']:,}")
        else:
            row += ['', '']
        
        f.write('| ' + ' | '.join(row) + ' |\n')

print("Done, announces.md created")
