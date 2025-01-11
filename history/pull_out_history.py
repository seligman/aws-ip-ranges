#!/usr/bin/env python3

from datetime import datetime
from hashlib import sha256
import json
import os
import subprocess

seen = set()
years = set()

cmd = "git rev-list --all --objects -- ../ip-ranges.json"
history = subprocess.check_output(cmd.split(' ')).decode("utf8")
for row in history.split("\n"):
    row = row.strip().split(' ')
    if len(row) == 2 and row[1] == "ip-ranges.json":
        print("Working on " + row[0], end="", flush=True)
        cmd = "git cat-file -p " + row[0]
        data = subprocess.check_output(cmd.split(' '))
        hash = sha256(data).hexdigest()
        if hash in seen:
            print(", dupe detected", flush=True)
        else:
            seen.add(hash)
            time = datetime(*[int(x) for x in json.loads(data)['createDate'][:19].split("-")])
            if os.path.isfile(time.strftime("%Y") + ".tar.gz") or os.path.isfile(time.strftime("%Y") + "_01.tar.gz"):
                print(", already archived " + time.strftime("%Y-%m-%d %H:%M:%S"), flush=True)
                break
            else:
                dn = time.strftime("%Y")
                years.add(dn)
                if not os.path.isdir(dn):
                    os.mkdir(dn)
                with open(os.path.join(dn, time.strftime("%Y-%m-%d-%H-%M-%S.json")), "wb") as f:
                    f.write(data)
                print(", created file for " + time.strftime("%Y-%m-%d %H:%M:%S"), flush=True)

for year in sorted(years)[:-1]:
    files = []
    for dirname, dirnames, filenames in os.walk(year):
        for fn in filenames:
            full_name = os.path.join(dirname, fn)
            files.append({
                'fn': fn,
                'full_name': full_name, 
                'size': os.path.getsize(full_name),
            })

    # Sort by filename, in other words, sort by date
    files.sort(key=lambda x: x['fn'])
    batches = []

    # Try to find the compression ratio
    test_batch = {
        "size": 0,
        "files": [],
    }
    for file in files:
        test_batch["size"] += file['size']
        test_batch["files"].append(file)
        if test_batch["size"] >= (50 * 1024 * 1024):
            break
    with open("_temp_files", "wt") as f:
        for cur in test_batch['files']:
            f.write(cur['full_name'] + "\n")
    dest_fn = "test_batch.tar.gz"
    cmd = f"tar --owner=0 --group=0 -T _temp_files -czf {dest_fn}"
    print("$ " + cmd)
    subprocess.check_call(cmd, shell=True)
    os.unlink('_temp_files')
    # Give ourselves a 10% buffer for future files
    test_batch["actual_compressed"] = os.path.getsize(dest_fn)
    test_batch["compressed"] = int(os.path.getsize(dest_fn) * 1.1)
    os.unlink(dest_fn)
    compression_ratio = test_batch['size'] / test_batch['compressed']
    print(f"# Got an expected ratio of {compression_ratio:.2f}")

    for file in files:
        # Given the test file compressed, try to limit filesize to 95 MiB
        if len(batches) == 0 or batches[-1]['size'] >= (95 * 1024 * 1024) * compression_ratio:
            batches.append({'files': [], 'size': 0, 'id': ''})
        batches[-1]['files'].append(file)
        batches[-1]['size'] += file['size']

    if len(batches) > 1:
        for i, batch in enumerate(batches):
            batch['id'] = f"_{i+1:02d}"

    for batch in batches:
        with open("_temp_files", "wt") as f:
            for cur in batch['files']:
                f.write(cur['full_name'] + "\n")
        dest_fn = f"{year}{batch['id']}.tar.gz"
        cmd = f"tar --owner=0 --group=0 -T _temp_files -czf {dest_fn}"
        print("$ " + cmd)
        subprocess.check_call(cmd, shell=True)
        os.unlink('_temp_files')
        actual_size = os.path.getsize(dest_fn)
        expected_size = int(batch['size'] / (test_batch['size'] / test_batch['actual_compressed']))
        print(f"# File size is {actual_size:,}, expected {expected_size:,}, that's {abs(expected_size - actual_size)/actual_size*100:.2f}% off")
        if os.path.getsize(dest_fn) >= 100 * 1024 * 1024:
            raise Exception(f"{dest_fn} is too big!")
    cmd = f"rm -rf {year}"
    print("$ " + cmd)
    subprocess.check_call(cmd, shell=True)
