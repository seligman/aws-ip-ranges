# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).  You 
can read more about the file [here](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).

This repository tracks changes to that file, and based off a trigger on the SNS topic 
automatically produces this chart showing how what percentage of the Internet's IPv4 
address space AWS is in control of.

{compare}

![History of AWS](history_count.svg)

# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
{changes}


# 15 largest changes to date:

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
{top10_changes}


[![RSS Icon](rss-icon.png)RSS Feed](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss.xml)
