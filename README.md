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

[Comparing other providers](https://github.com/seligman/cloud_sizes), as of 2022-07-27, Microsoft's Azure has 26998917 IPs, or 0.73%, and Google Cloud has 10532608 IPs, or 0.28%.

![History of AWS](history_count.svg)

# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2022-07-27 05:13:05 | 1.80190 | 66710940 | +320 | +15.230.248.0/24, +13.34.18.128/26 |
| 2022-07-26 15:33:07 | 1.80189 | 66710620 | +64 | +13.34.79.0/26 |
| 2022-07-26 00:53:05 | 1.80189 | 66710556 | +2 | +150.222.232.226/31 |
| 2022-07-25 01:13:05 | 1.80211 | 66718746 | +256 | +15.230.247.0/24 |
| 2022-07-22 22:03:05 | 1.80210 | 66718490 | +16640 | +18.88.128.0/18, +104.153.113.0/24 |
| 2022-07-22 20:23:05 | 1.80165 | 66701850 | +256 | +104.153.112.0/24 |
| 2022-07-22 15:03:08 | 1.80165 | 66701594 | +65536 | +18.68.0.0/16 |
| 2022-07-22 08:13:05 | 1.79988 | 66636058 | +128 | +13.34.78.128/25 |
| 2022-07-21 22:13:05 | 1.79987 | 66635930 | +8192 | +16.12.64.0/19 |
| 2022-07-21 16:13:06 | 1.79965 | 66627738 | +8192 | +16.12.32.0/19 |
| 2022-07-21 08:23:05 | 1.79943 | 66619546 | +2 | +150.222.232.224/31 |
| 2022-07-21 02:13:05 | 1.79943 | 66619544 | +256 | +15.230.168.0/24 |
| 2022-07-15 14:13:05 | 1.79942 | 66619288 | +256 | +3.4.8.0/24 |
| 2022-07-15 07:13:07 | 1.79942 | 66619032 | +32 | +13.34.78.32/27 |
| 2022-07-14 06:03:05 | 1.79942 | 66619000 | +256 | +15.230.194.0/24 |


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
