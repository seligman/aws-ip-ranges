# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).

This repository tracks changes to that file, and produces this
chart showing how what percentage of the Internet's IPv4 address space
AWS is in control of:

![History of AWS](history_count.png)

*As of {time}*:

AWS has {aws} public IPv4 addresses.

That represents {aws_perc}% of the possible IPs.
