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
        for region in regions:
            firsts[region] = min(firsts.get(region, data['createDate']), data['createDate'])

    with open("first_seens.json", "wt") as f:
        json.dump(firsts, f, indent=4, sort_keys=True)
        f.write("\n")

if __name__ == "__main__":
    main()
