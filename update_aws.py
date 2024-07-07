#!/usr/bin/env python3

from datetime import datetime, timedelta
from netaddr import IPSet, IPNetwork
from urllib.request import urlopen
import aws_ipv4_size
import json
import matplotlib.pyplot as plt
import matplotlib
import os
import re
import subprocess
import sys
if sys.version_info >= (3, 11): from datetime import UTC
else: import datetime as datetime_fix; UTC=datetime_fix.timezone.utc

def comma_dec(number, dec=0, show_positive=False):
    start = ""
    if number < 0:
        start = "-"
        number = -number
    elif show_positive:
        start = "+"
    number += 0.5 / pow(10, dec)
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    ret = s + ','.join(reversed(groups))
    if dec > 0:
        ret += (".%0" + str(dec) + "d") % (int((number - int(number)) * pow(10, dec)), )
    return start + ret

_started = datetime.now(UTC).replace(tzinfo=None)
def log_step(value):
    # Simple helper to show how long everything takes
    print(f"{(datetime.now(UTC).replace(tzinfo=None) - _started).total_seconds():8.4f}: {value}", flush=True)

class Cache:
    def __init__(self, filename, sort_keys=None):
        self.sort_keys = sort_keys
        self.filename = filename
        self.data = {}
        if os.path.isfile(filename):
            with open(filename) as f:
                self.data = json.load(f)
    def get_sorted(self):
        temp = [(x, json.dumps(y, separators=(",", ":"))) for x,y in self.data.items()]
        temp.sort(key=lambda x: x[1])
        return temp
    def save(self):
        with open(self.filename, "w", encoding="utf-8", newline="") as f:
            # We're doing this manually to make the file a bit smaller
            # Do this in order of the update just so it's easier to view
            f.write("{\n")
            if self.sort_keys is None:
                temp = self.get_sorted()
            else:
                temp = self.sort_keys.get_sorted()
                temp = [(x, json.dumps(self.data[x], separators=(",", ":"))) for x,_ in temp]
            f.write(",\n".join(f"{json.dumps(x)}:{y}" for x,y in temp))
            f.write("\n}\n")
    def __contains__(self, key): return key in self.data
    def __getitem__(self, key): return self.data[key]
    def __setitem__(self, key, value): self.data[key] = value
    def __iter__(self): return self.data.__iter__()
    def items(self): return self.data.items()
    def values(self): return self.data.values()

force = False
if len(sys.argv) > 1 and sys.argv[1] == "force":
    log_step("Force flag in effect")
    force = True

# Load the old firsts file, if it exists
firsts = Cache("first_seens.json")
firsts_changed = False

# First off, see if the live file has changed
log_step("Getting AWS's IP ranges file")
ip_ranges = urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json").read()
log_step("Importing old data")
with open("ip-ranges.json") as f:
    ip_ranges_old = json.load(f)
log_step("Decoding current data")
ip_ranges_cur = json.loads(ip_ranges)

log_step("Note any new regions and services")
all_regions = set(x['region'] for x in ip_ranges_cur['prefixes'])
all_services = set(x['service'] for x in ip_ranges_cur['prefixes'])
for value in all_regions | all_services:
    if value not in firsts:
        firsts[value] = ip_ranges_cur['createDate']
        firsts_changed = True

if firsts_changed:
    firsts.save()

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
        log_step("No changes, all done")
        # Nothing changed, just call it quits
        exit(0)

# Now, build up our cache of history, use a couple of helper functions
# to make loading and saving them easier
changed = False

log_step("Load some stats from history")
cache = Cache("history_count.json")
changes = Cache("history_changes.json", sort_keys=cache)

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
    cache.save()
    changes.save()

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
            values[time_str][2] = max(values[time_str][2], value[4])
        else:
            values[time_str] = [time, value[1], value[4]]

    # And create two lists, one of days, and one as 
    # the percent values to chart
    log_step("Organize the summary")
    keys = sorted(values)

    # Add any missing dates, so it's more obvious when changes happened in the past
    cur, end = values[min(keys)][0], values[max(keys)][0]
    last = cur.strftime("%Y-%m-%d")
    while cur <= end:
        cur_day = cur.strftime("%Y-%m-%d")
        if cur_day not in values:
            temp = values[last]
            values[cur_day] = [cur, temp[1], temp[2]]
        last = cur_day
        cur += timedelta(days=1)
    keys = sorted(values)

    # Limit the range of data shown in the chart
    max_years = 8
    if (values[keys[-1]][0] - values[keys[0]][0]) > timedelta(days=365.25*max_years):
        for i in range(len(keys)):
            if (values[keys[-1]][0] - values[keys[i]][0]) <= timedelta(days=365.25*max_years):
                keys = keys[i:]
                break

    # Simplify the data for charting
    dates = [values[x][0] for x in keys]
    counts = [values[x][2] for x in keys]
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
    # Draw the axis lines for precise control over where they show up
    temp = min(dates)
    temp = datetime(temp.year, 1, 1)
    while temp < max(dates):
        plt.axvline(temp, color=(0.8, 0.8, 0.8), linewidth=1)
        temp = datetime(temp.year + 1, 1, 1)
    temp = 0
    while temp < max(values):
        plt.axhline(temp, color=(0.8, 0.8, 0.8), linewidth=1)
        temp += 0.25
    # Draw the plot itself
    plt.plot(dates, values, linewidth=2)
    # Add some padding to the x axis to suggest future dates
    pad = timedelta(seconds=(max(dates) - min(dates)).total_seconds() * 0.025)
    plt.xlim(min(dates), max(dates) + pad)
    # And pad the top of the chart to leave room for event labels
    pad = (max(values) - min(values)) * 0.15
    plt.ylim(0, max(values) + pad)

    # Find all the candidates for annotations
    targets = []
    # Start at an offset to give plenty of room for the first annotation
    last_val = 0
    last_day = None
    for i, (day, perc_ipv4, value) in enumerate(zip(dates, values, counts)):
        # Only look at changes of more than 100k
        diff = value - last_val
        if i > 0 and abs(diff) >= 100000:
            if (day - last_day) < timedelta(days=2):
                targets.append({
                    'target': 0 if diff > 0 else 1,
                    'diff': diff,
                    'i': i,
                    'date': day,
                    'run': 1,
                    'perc_ipv4': perc_ipv4,
                })
        last_val = value
        last_day = day

    # Merge events that span two or more days
    last_val = None
    for value in targets:
        if last_val is not None:
            if last_val['i'] + 1 == value['i']:
                if (last_val['diff'] > 0) == (value['diff'] > 0):
                    value['diff'] += last_val['diff']
                    value['run'] += last_val['run']
                    last_val['merged'] = True
        last_val = value

    # Remove any elements that were merged into the following days
    targets = [x for x in targets if 'merged' not in x]

    # Only keep 6 months and on, to give ourselves plenty of padding at the start
    start_at = dates[0] + timedelta(days=180)
    targets = [x for x in targets if x['date'] >= start_at]

    # Drop any change below 1.5m IPs added / removed
    targets = [x for x in targets if abs(x['diff']) >= 1500000]

    # Limit the annotations to only show one every so often
    picked = []
    targets.sort(key=lambda x: (-abs(x['diff']), x['i']))
    for cur in targets:
        use = True
        for other in picked:
            if other['target'] == cur['target']:
                if abs((other['date'] - cur['date']).total_seconds() / 86400) <= 270:
                    use = False
                    break
        if use:
            picked.append(cur)
    picked.sort(key=lambda x: x['i'])

    # Draw out the picked labels
    for cur in picked:
        label = f'{cur["date"].strftime("%Y-%m-%d")}'
        label += f'\n {"+-"[cur["target"]]}{abs(cur["diff"])/1000000:.2f}m '
        args = {
            'text': label,
            'xy': [cur['date'], cur['perc_ipv4']], 
            'xytext': [cur['date'], cur['perc_ipv4']], 
            'bbox': {"boxstyle": "round", "fc":"0.8"},
            'arrowprops': {"arrowstyle": "-"},
            'fontsize': 'small',
        }
        if cur['target'] == 0:
            args['xytext'][0] -= timedelta(days=400)
            args['xytext'][1] += 0.05
        else:
            args['xytext'][0] += timedelta(days=50)
            args['xytext'][1] -= 0.3
        plt.annotate(**args)

    # Ensure the IDs in the SVG have a consistent value
    matplotlib.rcParams['svg.hashsalt'] = "0"
    plt.savefig("history_count.svg", bbox_inches='tight')
    # Normalize the SVG to prevent churn if it fundamentally hasn't changed
    with open("history_count.svg", "rt", newline="", encoding="utf-8") as f:
        temp = f.read()
    temp = re.sub("<metadata>.*</metadata>", "", temp, flags=re.DOTALL)
    with open("history_count.svg", "wt", newline="", encoding="utf-8") as f:
        f.write(temp)

    log_step("Filling out template")
    with open("README.template.md", "rt") as f:
        md = f.read()
    
    log_step("Getting comparision data")
    others = json.loads(urlopen("https://raw.githubusercontent.com/seligman/cloud_sizes/master/data/summary.json").read())
    not_private_size = 3702258432
    compare = f"[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of {others['_'][:10]}:\n\n"
    compare += "| | IPs | Percent |\n| --- | ---: | ---: |\n"
    compare += f"| Amazon AWS | {comma_dec(in_order[-1][4])} | {in_order[-1][1]*100:0.5f} |\n"
    compare += f"| Microsoft Azure | {comma_dec(others['azure'][0])} | {others['azure'][0]/not_private_size*100:0.5f} |\n"
    compare += f"| Google Cloud | {comma_dec(others['google'][0])} | {others['google'][0]/not_private_size*100:0.5f} |\n"
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
                (
                    f"| {item[0].replace(' ', '&nbsp;').replace('-', '&#8209;')} |" + 
                    f" {item[1]*100.0:.5f} |" + 
                    f" {comma_dec(item[4])} |" + 
                    f" {comma_dec(diff, show_positive=True)} |" + 
                    f" {', '.join(cidrs).replace(' ', '&nbsp;')} |"
                ),
                item[0],
                f"{'+' if diff > 0 else ''}{diff}",
                all_cidrs,
            ))
        last_count = item[4]

    rss_history = all_history[:]

    for key, value in firsts.items():
        seen_at = datetime(*[int(x) for x in value.split("-")]).strftime("%Y-%m-%d %H:%M:%S")
        msg = None
        if key in all_regions:
            msg = f"Region {key}"
        elif key in all_services:
            msg = f"Service {key}"
        if msg is not None:
            all_history.append((
                1,
                f"| {seen_at.replace(' ', '&nbsp;').replace('-', '&#8209;')} | | | | {msg} |",
                seen_at,
                "+0",
                [],
            ))
    all_history.sort(key=lambda x:x[2])

    log_step("Getting history")
    history = [x[1] for x in all_history if abs(x[0]) > 0][:-16:-1]
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
    # Create two RSS feeds, one with only big changes it in
    for opts in [{"fn": "rss.xml"}, {"fn": "rss_big_changes.xml", "big_changes": True}]:
        with open(opts['fn'], "wt", encoding="utf-8", newline="") as f:
            base_url = "https://github.com/seligman/aws-ip-ranges"

            f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
            f.write('<rss version="2.0">\n')
            f.write('  <channel>\n')
            f.write('    <title>AWS IP Ranges Updates</title>\n')
            f.write(f'    <link>{base_url}</link>\n')
            f.write("    <description>Changes to AWS's IP Ranges</description>\n")

            bail = 20
            log_step("Filling out the RSS feed")
            for cur in rss_history[::-1]:
                show_item = True
                if opts.get("big_changes", False):
                    if abs(cur[3]) <= 5000:
                        show_item = False
                
                if show_item:
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
                    bail -= 1
                    if bail == 0:
                        break
            
            # Also log the newest regions and services, so feed readers will show it
            bail_at = datetime.now(UTC).replace(tzinfo=None) - timedelta(days=30)
            regions = [(value, key) for key, value in firsts.items()]
            regions.sort(reverse=True)
            for seen_at, value in regions:
                seen_at = seen_at[:19]
                if value in all_regions:
                    f.write('    <item>\n')
                    f.write(f'      <title>AWS {value} Region Detected</title>\n')
                    f.write(f'      <link>{base_url}#{(value + seen_at).replace(" ", "").replace("-", "").replace(":", "")}</link>\n')
                    f.write('      <description><![CDATA[\n')
                    seen_at = datetime(*[int(x) for x in seen_at.split("-")])
                    f.write(f"AWS Region {value} detected at {seen_at.strftime('%Y-%m-%d %H:%M:%S')}<br>\n")
                    f.write(']]></description>\n')
                    f.write('    </item>\n')
                elif value in all_services:
                    f.write('    <item>\n')
                    f.write(f'      <title>AWS {value} Service Detected</title>\n')
                    f.write(f'      <link>{base_url}#{(value + seen_at).replace(" ", "").replace("-", "").replace(":", "")}</link>\n')
                    f.write('      <description><![CDATA[\n')
                    seen_at = datetime(*[int(x) for x in seen_at.split("-")])
                    f.write(f"AWS Service {value} detected at {seen_at.strftime('%Y-%m-%d %H:%M:%S')}<br>\n")
                    f.write(']]></description>\n')
                    f.write('    </item>\n')
                if seen_at < bail_at:
                    break

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
        subprocess.check_call(["git", "add", "rss_big_changes.xml"])
        subprocess.check_call(["git", "add", "README.md"])

        log_step("Creating git commit")
        subprocess.check_call(["git", "commit", "-a", "-m", "Update data files"])

        # Push the results
        log_step("Pushing changes")
        subprocess.check_call(["git", "push"])

log_step("All done")
