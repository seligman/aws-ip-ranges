#!/usr/bin/env python3

import json

# Load the region data, announces.json is manually updated
with open("announces.json") as f:
    data = json.load(f)

# Create a pretty version of the data file
with open("announces.md", "wt", newline="", encoding="utf-8") as f:
    f.write("# AWS Regions\n")
    f.write("\n")
    f.write("This file is generated from the [source data](announces.json), which ")
    f.write("is manually updated as new regions show up in ip-ranges.json, and when ")
    f.write("regions are publicly announced.")
    f.write("\n")
    f.write("| Region | ip-ranges.json | Announced | Days |\n")
    f.write("| :--- | :--- | :--- | ---: |\n")
    for cur in data:
        row = [
            cur['region'], 
            cur['appeared_ip_ranges'],
        ]
        if 'announced' in cur and 'days_to_announce' in cur and 'announce_url' in cur:
            row.append("[" + cur['announced'] + "](" + cur['announce_url'] + ")")
            row.append(f"{cur['days_to_announce']:,}")
        else:
            row += ['', '']
        
        f.write('| ' + ' | '.join(row) + ' |\n')

print("Done, announces.md created")
