#!/usr/bin/env python3

# Simple tool to find the first seen for all regions

import os
import json
import tarfile

def get_history():
    # Load all history files, including history files inside of .tar.gz files
    for cur in os.listdir("history"):
        cur = os.path.join("history", cur)
        if cur.endswith(".tar.gz"):
            with tarfile.open(cur, "r:gz") as tar:
                for obj in tar:
                    yield json.load(tar.extractfile(obj))
        elif os.path.isdir(cur):
            for fn in os.listdir(cur):
                with open(os.path.join(cur, fn)) as f:
                    yield json.load(f)

def main():
    firsts = {}

    for data in get_history():
        regions = set(x['region'] for x in data['prefixes'])
        services = set(x['service'] for x in data['prefixes'])
        for region in regions | services:
            firsts[region] = min(firsts.get(region, data['createDate']), data['createDate'])

    with open("first_seens.json", "w", encoding="utf-8", newline="") as f:
        f.write("{\n")
        temp = [(x, json.dumps(y, separators=(",", ":"))) for x,y in firsts.items()]
        temp.sort(key=lambda x: (x[1], x[0]))
        f.write(",\n".join(f"{json.dumps(x)}:{y}" for x,y in temp))
        f.write("\n}\n")

if __name__ == "__main__":
    main()
