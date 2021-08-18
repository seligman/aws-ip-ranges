#!/usr/bin/env python3

import subprocess
from hashlib import sha256
import json
from datetime import datetime
import os

"""
YEAR=2015 ; find ${YEAR} -type f | sort | tar --owner=0 --group=0 -T - -cvzf ${YEAR}.tar.gz
"""

seen = set()

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
            if os.path.isfile(time.strftime("%Y") + ".tar.gz"):
                print(", already archived " + time.strftime("%Y-%m-%d %H:%M:%S"), flush=True)
                break
            else:
                dn = time.strftime("%Y")
                if not os.path.isdir(dn):
                    os.mkdir(dn)
                with open(os.path.join(dn, time.strftime("%Y-%m-%d-%H-%M-%S.json")), "wb") as f:
                    f.write(data)
                print(", created file for " + time.strftime("%Y-%m-%d %H:%M:%S"), flush=True)
