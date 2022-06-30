#!/usr/bin/env python3

import json
import os
import sys
import subprocess
import aws_ipv4_size
from datetime import datetime
import matplotlib.pyplot as plt
from requests import get
from netaddr import IPSet, IPNetwork

started = datetime.utcnow()
def log_step(value):
    # Simple helper to show how long everything takes
    print(f"{(datetime.utcnow() - started).total_seconds():8.4f}: {value}", flush=True)

force = False
if len(sys.argv) > 1 and sys.argv[1] == "force":
    log_step("Force flag in effect")
    force = True

# Load the old firsts file, if it exists
if os.path.isfile("first_seens.json"):
    with open("first_seens.json") as f:
        firsts = json.load(f)
else:
    firsts = {}
firsts_changed = False

# First off, see if the live file has changed
log_step("Getting AWS's IP ranges file")
ip_ranges = get("https://ip-ranges.amazonaws.com/ip-ranges.json").content
log_step("Importing old data")
with open("ip-ranges.json") as f:
    ip_ranges_old = json.load(f)
log_step("Decoding current data")
ip_ranges_cur = json.loads(ip_ranges)

log_step("Note any new regions")
all_regions = set(x['region'] for x in ip_ranges_cur['prefixes'])
for region in all_regions:
    if region not in firsts:
        firsts[region] = ip_ranges_cur['createDate']
        firsts_changed = True
if firsts_changed:
    with open("first_seens.json", "wt") as f:
        json.dump(firsts, f, indent=4, sort_keys=True)
        f.write("\n")

log_step("Initial load done, checking for changes")
if ip_ranges_cur['createDate'] != ip_ranges_old['createDate']:
    # Ok, the live file has change, write out a bit-for-bit copy
    # to our local copy
    log_step("Updating ip-ranges.json")
    with open("ip-ranges.json", "wb") as f:
        f.write(ip_ranges)
    
    log_step("Parsing date from IP ranges")
    # Crack out the date from the data file
    time = datetime(*[int(x) for x in ip_ranges_cur['createDate'][:19].split("-")])
    # Turn that into the format git expects
    git_time = time.strftime("%a %b %d %H:%M:%S %Y +0000")
    # Back date the commit (and the next one) to when this file was updated
    os.environ['GIT_COMMITTER_DATE'] = git_time
    os.environ['GIT_AUTHOR_DATE'] = git_time
    # Commit the change to ip-ranges.json to git
    if not force:
        log_step("Staging IP ranges file")
        subprocess.check_call(["git", "add", "ip-ranges.json"])
        if firsts_changed:
            log_step("Staging firsts data file")
            subprocess.check_call(["git", "add", "first_seens.json"])
        log_step("Commit IP ranges file")
        subprocess.check_call(["git", "commit", "-a", "-m", f"ip-ranges from {time.strftime('%Y-%m-%d %H:%M:%S')}"])
else:
    if not force:
        # Nothing changed, just call it quits
        exit(0)

# Now, build up our cache of history, use a couple of helper functions
# to make loading and saving them easier
changed = False
def load_cache(filename):
    if os.path.isfile(filename):
        with open(filename) as f:
            return json.load(f)
    else:
        return {}
def save_cache(filename, data):
    with open(filename, "w") as f:
        # We're doing this manually to make the file a bit smaller
        # Do this in order of the update just so it's easier to view
        f.write("{\n")
        f.write(",\n".join([f'"{x}":{json.dumps(data[x], separators=(",", ":"))}' for x in sorted(cache, key=lambda y:cache[y][0])]))
        f.write("\n}\n")

log_step("Load some stats from history")
cache = load_cache("history_count.json")
changes = load_cache("history_changes.json")

log_step("Look for all historical git objects")
# Pull out all of the history items for this file:
cmd = "git rev-list --all --objects -- ip-ranges.json"
history = subprocess.check_output(cmd.split(' ')).decode("utf8")
for row in history.split("\n"):
    row = row.strip().split(' ')
    if len(row) == 2 and row[1] == "ip-ranges.json":
        # If there's a history item we haven't parsed, pull
        # the data and parse it
        if row[0] not in cache:
            log_step(f"Loading {row[0]}")
            cmd = "git cat-file -p " + row[0]
            data = subprocess.check_output(cmd.split(' '))
            data = json.loads(data)

            # Call our helper to get a count of how many IP addresses
            # are in this file
            public, internet, aws = aws_ipv4_size.parse_aws(data)
            aws_perc = aws / public

            # Store the final value back in our cache
            time = datetime(*[int(x) for x in data['createDate'][:19].split("-")])
            cache[row[0]] = [time.strftime("%Y-%m-%d %H:%M:%S"), aws_perc, public, internet, aws]
            changed = True

# And track all of the changes to the addresses as well
last_key = None
for key in sorted(cache, key=lambda y:cache[y][0]):
    if key not in changes:
        log_step(f"Loading addresses from {key}")
        changed = True
        if last_key is None:
            changes[key] = {"added": [], "removed": []}
        else:
            def load_data(key):
                cmd = "git cat-file -p " + key
                data = subprocess.check_output(cmd.split(' '))
                data = json.loads(data)
                return IPSet([IPNetwork(x["ip_prefix"]) for x in data["prefixes"]])
            aws = load_data(key)
            last_aws = load_data(last_key)
            def get_diff(a, b):
                diff = a - b
                diff = [IPNetwork(x) for x in diff.iter_cidrs()]
                diff = sorted(diff, key=lambda x:x.size, reverse=True)
                return [str(x) for x in diff]
            changes[key] = {"added": get_diff(aws, last_aws), "removed": get_diff(last_aws, aws)}
    last_key = key

if changed or force:
    log_step("Saving cache files")
    # Something changed, go ahead and write things out
    save_cache("history_count.json", cache)
    save_cache("history_changes.json", changes)

    # Pull in the days in the history, using the largest
    # value for the day when there are multiple entries for
    # one day
    log_step("Summarize the history")
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
    log_step("Organize the summary")
    keys = sorted(values)
    dates = [values[x][0] for x in keys]
    values = [values[x][1] * 100.0 for x in keys]

    # And also make a sorted list for the information dump
    in_order = [cache[x]+[x] for x in sorted(cache, key=lambda y:cache[y][0])]

    log_step("Charting data")
    # Chart everything out
    plt.rcParams.update({
        "axes.facecolor":    (0.9, 0.9, 0.9, 1),
        "savefig.facecolor": (0.7, 0.7, 0.7, 1),
    })

    plt.figure(figsize=(9, 5))
    plt.title("History of percentage of AWS ownership of IPv4 space")
    plt.plot(dates, values)
    plt.savefig("history_count.svg", bbox_inches='tight')

    log_step("Filling out template")
    with open("README.template.md", "rt") as f:
        md = f.read()
    
    log_step("Getting comparision data")
    others = get("https://raw.githubusercontent.com/seligman/cloud_sizes/master/data/summary.json").json()
    not_private_size = 3702258432
    compare = f"[Comparing other providers](https://github.com/seligman/cloud_sizes), as of {others['_'][:10]}, "
    compare += f"Microsoft's Azure has {others['azure'][0]} IPs, or {others['azure'][0]/not_private_size*100:0.2f}%, and "
    compare += f"Google Cloud has {others['google'][0]} IPs, or {others['google'][0]/not_private_size*100:0.2f}%."
    md = md.replace("{compare}", compare)

    log_step("Creating items for tables")
    all_history = []
    last_count = None
    for item in in_order:
        if last_count is not None:
            diff = item[4] - last_count
            all_cidrs = ['+'+x for x in changes[item[5]]['added']] + ['-'+x for x in changes[item[5]]['removed']]
            if len(all_cidrs) > 3:
                cidrs = all_cidrs[:3] + ['...']
            else:
                cidrs = all_cidrs
            all_history.append((
                diff, 
                f"| {item[0]} |" + 
                f" {item[1]*100.0:.5f} |" + 
                f" {item[4]} |" + 
                f" {'+' if diff > 0 else ''}{diff} |" + 
                f" {', '.join(cidrs)} |",
                item[0],
                f"{'+' if diff > 0 else ''}{diff}",
                all_cidrs,
            ))
        last_count = item[4]

    log_step("Getting history")
    history = [x[1] for x in all_history if x[0] > 0][:-16:-1]
    # Note that when we sort the top items we take the absolute value of the change
    # to show the big removals as well as the big adds.  All the other data is added
    # to the sort key to make it a stable sort for the cases where two changes
    # were the same size.
    log_step("Getting overall top items")
    top_history = [x[1] for x in sorted(all_history, key=lambda y:(abs(y[0]), y))[-15:]][::-1]

    log_step("Creating the tables")
    # Drop in the tables into the markdown document
    md = md.replace("{changes}", "\n".join(history))
    md = md.replace("{top10_changes}", "\n".join(top_history))
    log_step("Writing out the new README")
    with open("README.md", "wt") as f:
        f.write(md)

    log_step("Creating an RSS feed")
    # Create an RSS feed, do it by hand just to make things easy
    with open("rss.xml", "wt") as f:
        base_url = "https://github.com/seligman/aws-ip-ranges"

        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        f.write('<rss version="2.0">\n')
        f.write('  <channel>\n')
        f.write('    <title>AWS IP Ranges Updates</title>\n')
        f.write(f'    <link>{base_url}</link>\n')
        f.write("    <description>Changes to AWS's IP Ranges</description>\n")

        log_step("Filling out the RSS feed")
        for cur in all_history[-20:]:
            f.write('    <item>\n')
            f.write(f'      <title>AWS IP Ranges update for {cur[2]}</title>\n')
            f.write(f'      <link>{base_url}#{cur[2].replace(" ", "").replace("-", "").replace(":", "")}</link>\n')
            f.write('      <description><![CDATA[\n')
            if len(cur[4]) == 0:
                f.write("No changes to IPs\n")
            else:
                f.write(f"Changed by {cur[3]}<br><br>\n")
                for cur_range in cur[4]:
                    if cur_range.startswith("+"):
                        f.write(f"Added {cur_range[1:]}<br>\n")
                    elif cur_range.startswith("-"):
                        f.write(f"Removed {cur_range[1:]}<br>\n")
                    else:
                        f.write(f"{cur_range}<br>\n")
            f.write(']]></description>\n')
            f.write('    </item>\n')

        f.write('  </channel>\n')
        f.write('</rss>\n')

    log_step("Done with most work")
    if not force:
        log_step("Staging files for git changes")
        # Commit all of the files that were changed
        subprocess.check_call(["git", "add", "history_count.json"])
        subprocess.check_call(["git", "add", "history_changes.json"])
        subprocess.check_call(["git", "add", "history_count.svg"])
        subprocess.check_call(["git", "add", "rss.xml"])
        subprocess.check_call(["git", "add", "README.md"])

        log_step("Creating git commit")
        subprocess.check_call(["git", "commit", "-a", "-m", "Update data files"])

        # Push the results
        log_step("Pushing changes")
        subprocess.check_call(["git", "push"])

log_step("All done")
