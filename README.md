# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).
You can read more about the file [here](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
If you want to look up an AWS IP address, you can search for its presence in ip-ranges.json using [this tool](https://seligman.github.io/aws-ip-ranges/).

This repository tracks changes to that file, and based off a trigger on the SNS topic 
automatically produces this chart showing how what percentage of the Internet's IPv4 
address space AWS is in control of.  Here's an 
[animation of the history](https://youtu.be/Su25yl7eol8) of the AWS's IP usage.

[![@aws_ip_changes on twitter](https://img.shields.io/twitter/url/https/twitter.com/aws_ip_changes.svg?style=social&label=%40aws_ip_changes)](https://twitter.com/aws_ip_changes) for updates as they happen.

[Comparing other providers](https://github.com/seligman/cloud_sizes), as of 2022-07-13, Microsoft's Azure has 27003843 IPs, or 0.73%, and Google Cloud has 10522368 IPs, or 0.28%.

![History of AWS](history_count.svg)

# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2022-07-13 07:23:05 | 1.79941 | 66618676 | +256 | +15.230.246.0/24 |
| 2022-07-12 10:13:09 | 1.79940 | 66618420 | +64 | +13.34.77.224/27, +13.34.78.0/27 |
| 2022-07-12 03:23:05 | 1.79940 | 66618356 | +256 | +15.230.245.0/24 |
| 2022-07-11 20:23:05 | 1.79939 | 66618100 | +256 | +15.230.180.0/24 |
| 2022-07-07 13:23:05 | 1.79938 | 66617844 | +64 | +13.34.21.192/27, +13.34.77.192/27 |
| 2022-07-06 19:23:05 | 1.79938 | 66617780 | +64 | +13.34.21.128/26 |
| 2022-07-06 09:23:05 | 1.79938 | 66617812 | +32 | +13.34.21.128/27 |
| 2022-07-06 01:03:05 | 1.79938 | 66617780 | +256 | +15.230.244.0/24 |
| 2022-07-04 01:23:05 | 1.79938 | 66617524 | +256 | +15.230.243.0/24 |
| 2022-07-01 17:23:05 | 1.79937 | 66617332 | +64 | +13.34.77.192/26 |
| 2022-07-01 07:13:05 | 1.79937 | 66617268 | +256 | +15.230.242.0/24 |
| 2022-06-30 19:23:05 | 1.79936 | 66617012 | +64 | +13.34.77.128/26 |
| 2022-06-29 22:23:05 | 1.79936 | 66616948 | +256 | +15.230.225.0/24 |
| 2022-06-28 16:13:07 | 1.79938 | 66617716 | +65536 | +43.218.0.0/16 |
| 2022-06-28 01:23:05 | 1.79761 | 66552180 | +256 | +15.230.240.0/24 |


# 15 largest changes to date:

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2021-08-12 18:31:15 | 1.75915 | 65128214 | +5505024 | +3.48.0.0/12, +35.96.0.0/12, +3.152.0.0/13, ... |
| 2020-08-11 16:19:14 | 1.50480 | 55711498 | +4194304 | +252.0.0.0/10 |
| 2020-08-12 19:21:14 | 1.39151 | 51517198 | -4194304 | -252.0.0.0/10 |
| 2017-06-29 22:42:11 | 0.74955 | 27750448 | +3429728 | +13.232.0.0/13, +34.240.0.0/13, +35.168.0.0/13, ... |
| 2019-08-01 20:03:05 | 1.24953 | 46260706 | +3145728 | +44.192.0.0/10, -3.192.0.0/12 |
| 2017-04-07 18:22:10 | 0.65692 | 24320720 | +3025152 | +34.208.0.0/12, +34.224.0.0/12, +13.58.0.0/15, ... |
| 2018-12-18 21:54:17 | 1.05392 | 39019010 | +2228224 | +3.208.0.0/12, +3.224.0.0/12, +13.48.0.0/15 |
| 2016-04-22 18:22:20 | 0.46701 | 17290016 | +2214656 | +52.200.0.0/13, +52.208.0.0/13, +52.36.0.0/14, ... |
| 2017-12-21 20:12:10 | 0.81440 | 30151184 | +1703936 | +18.208.0.0/13, +18.204.0.0/14, +18.224.0.0/14, ... |
| 2018-08-22 21:22:35 | 0.95738 | 35444840 | +1572864 | +3.80.0.0/12, +3.16.0.0/14, +3.40.0.0/14 |
| 2019-07-30 16:43:04 | 1.16456 | 43114908 | +1310720 | +3.192.0.0/12, +15.222.0.0/15, +15.236.0.0/15 |
| 2016-09-21 12:34:06 | 0.54213 | 20071088 | +1310720 | +34.192.0.0/12, +35.156.0.0/14, +52.219.68.0/22, ... |
| 2021-08-05 18:21:13 | 1.61044 | 59622723 | +1048576 | +43.192.0.0/12 |
| 2020-10-22 18:31:17 | 1.47052 | 54442529 | +1048576 | +3.64.0.0/12 |
| 2020-09-28 13:51:16 | 1.42963 | 52928471 | +1048576 | +35.80.0.0/12 |


[![RSS Icon](rss-icon.png)RSS Feed](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss.xml)
