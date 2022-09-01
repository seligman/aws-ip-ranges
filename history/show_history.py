#!/usr/bin/env python3

import tarfile
import json
import os
from netaddr import IPSet, IPNetwork
from datetime import datetime

def get_history():
    # Load all history files, including history files inside of .tar.gz files
    for cur in sorted(os.listdir(".")):
        if cur.endswith(".tar.gz"):
            with tarfile.open(cur, "r:gz") as tar:
                for obj in tar:
                    yield json.load(tar.extractfile(obj))
        elif os.path.isdir(cur):
            for fn in sorted(os.listdir(cur)):
                with open(os.path.join(cur, fn)) as f:
                    yield json.load(f)

def main():
    print(",ipv4_count,ipv6_count")
    for data in get_history():
        # TODO: Do something interesting with the files
        created = datetime(*map(int, data['createDate'][:19].split("-")))
        ipv4 = IPSet(IPNetwork(x['ip_prefix']) for x in data.get('prefixes', []))
        ipv6 = IPSet(IPNetwork(x['ipv6_prefix']) for x in data.get('ipv6_prefixes', []))
        print(",".join([created.strftime("%Y-%m-%d %H:%M:%S"), str(ipv4.size), str(ipv6.size)]))

if __name__ == "__main__":
    main()
