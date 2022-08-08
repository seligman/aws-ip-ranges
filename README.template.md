# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).
You can read more about the file [here](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
If you want to look up an AWS IP address, you can search for its presence in ip-ranges.json using [this tool](https://seligman.github.io/aws-ip-ranges/).

This repository tracks changes to that file, and based off a trigger on the SNS topic 
automatically produces this chart showing how what percentage of the Internet's IPv4 
address space AWS is in control of.  Here's an 
[animation of the history](https://youtu.be/Su25yl7eol8) of the AWS's IP usage.

To get updates as they happen:

[![@aws_ip_changes on twitter](https://shields.io/badge/-%40aws__ip__changes-black?logo=twitter&style=flat)](https://twitter.com/aws_ip_changes) [![RSS Icon](https://shields.io/badge/-RSS%20Feed-black?logo=rss&style=flat)](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss.xml)

![History of AWS](history_count.svg)

{compare}

# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
{changes}


# 15 largest changes to date:

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
{top10_changes}
