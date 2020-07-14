#!/usr/bin/env python3

import json
import os
import subprocess
import aws_ipv4_size
from datetime import datetime
import matplotlib.pyplot as plt
from requests import get

# First off, see if the live file has changed
ip_ranges = get("https://ip-ranges.amazonaws.com/ip-ranges.json").content
with open("ip-ranges.json") as f:
    ip_ranges_old = json.load(f)
ip_ranges_cur = json.loads(ip_ranges)
if ip_ranges_cur['createDate'] != ip_ranges_old['createDate']:
    # Ok, the live file has change, write out a bit-for-bit copy
    # to our local copy
    with open("ip-ranges.json", "wb") as f:
        f.write(ip_ranges)
    
    # Crack out the date from the data file
    time = datetime(*[int(x) for x in ip_ranges_cur['createDate'][:19].split("-")])
    # Turn that into the format git expects
    git_time = time.strftime("%a %b %d %H:%M:%S %Y +0000")
    # Back date the commit (and the next one) to when this file was updated
    os.environ['GIT_COMMITTER_DATE'] = git_time
    os.environ['GIT_AUTHOR_DATE'] = git_time
    # Commit the change to ip-ranges.json to git
    subprocess.check_call(["git", "add", "ip-ranges.json"])
    subprocess.check_call(["git", "commit", "-a", "-m", f"ip-ranges from {time.strftime('%Y-%m-%d %H:%M:%S')}"])

# Now, build up our cache of history
cache = {}
changed = False
if os.path.isfile("history_count.json"):
    with open("history_count.json") as f:
        cache = json.load(f)

# Pull out all of the history items for this file:
cmd = "git rev-list --all --objects -- ip-ranges.json"
history = subprocess.check_output(cmd.split(' ')).decode("utf8")
for row in history.split("\n"):
    row = row.strip().split(' ')
    if len(row) == 2 and row[1] == "ip-ranges.json":
        # If there's a history item we haven't parsed, pull
        # the data and parse it
        if row[0] not in cache:
            print(f"Loading {row[0]}...")
            cmd = "git cat-file -p " + row[0]
            data = subprocess.check_output(cmd.split(' '))
            data = json.loads(data)

            # Call our helper to get a count of how many IP addresses
            # are in this file
            public, _internet, aws = aws_ipv4_size.parse_aws(data)
            aws = aws / public

            # Store the final value back in our cache
            time = datetime(*[int(x) for x in data['createDate'][:19].split("-")])
            cache[row[0]] = [time.strftime("%Y-%m-%d %H:%M:%S"), aws]
            changed = True

if changed:
    # Something changed, go ahead and write things out
    with open("history_count.json", "w") as f:
        json.dump(cache, f, indent=2, sort_keys=True)
        f.write("\n")

    # Pull in the days in the history, using the largest
    # value for the day when there are multiple entries for
    # one day
    values = {}
    for value in cache.values():
        time_str = value[0][:10]
        time = datetime.strptime(time_str, "%Y-%m-%d")
        if time_str in values:
            values[time_str][1] = max(values[time_str][1], value[1])
        else:
            values[time_str] = [time, value[1]]

    # And create two lists, one of days, and one as 
    # the percent values to chart
    keys = sorted(values)
    dates = [values[x][0] for x in keys]
    values = [values[x][1] * 100.0 for x in keys]

    # Chart everything out
    plt.figure(figsize=(10,7))
    plt.plot(dates, values)
    plt.savefig("history_count.png")

    # Commit the cache file, and the .png file
    subprocess.check_call(["git", "add", "history_count.json"])
    subprocess.check_call(["git", "add", "history_count.png"])
    subprocess.check_call(["git", "commit", "-a", "-m", "Update data files"])

    # Push the results
    subprocess.check_call(["git", "push"])
