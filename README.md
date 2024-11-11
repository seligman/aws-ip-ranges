# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).
You can read more about the file [here](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
If you want to look up an IP address, you can see if it's from any of the cloud providers using [this tool](https://cloud-ips.s3-us-west-2.amazonaws.com/index.html).

This repository tracks changes to that file, and based off a trigger on the SNS 
topic automatically produces this chart showing how what percentage of the 
Internet's IPv4 address space AWS is in control of.  Here's some 
more [information about when different regions](announces.md) came 
online, and here's an [animation of the history](https://youtu.be/Su25yl7eol8) 
of the AWS's IP usage.

To get updates as they happen:

[![RSS Icon (Full Feed)](images/rss_badge.svg)](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss.xml)
[![RSS Icon (Large Changes)](images/rss_badge_partial.svg)](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss_big_changes.xml)

![History of AWS](history_count.svg)

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2024-11-12:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 80,092,433 | 2.16334 |
| Microsoft Azure | 44,719,730 | 1.20790 |
| Google Cloud | 14,529,792 | 0.39246 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2024&#8209;11&#8209;11&nbsp;23:43:10 | 2.16334 | 80,092,433 | +53 | +150.222.53.224/27,&nbsp;+3.4.15.152/29,&nbsp;+3.4.15.160/29,&nbsp;... |
| 2024&#8209;11&#8209;11&nbsp;18:13:08 | 2.16334 | 80,092,380 | +32 | +150.222.45.96/27 |
| 2024&#8209;11&#8209;09&nbsp;00:43:11 | 2.16334 | 80,092,348 | -512 | -192.157.36.0/23 |
| 2024&#8209;11&#8209;08&nbsp;17:23:08 | 2.16335 | 80,092,860 | -1,024 | -52.129.208.0/22 |
| 2024&#8209;11&#8209;07&nbsp;23:43:07 | 2.16338 | 80,093,884 | +512 | +192.157.36.0/23 |
| 2024&#8209;11&#8209;05&nbsp;16:43:11 | 2.16337 | 80,093,372 | +131,072 | +3.174.0.0/15 |
| 2024&#8209;11&#8209;01&nbsp;16:23:07 | 2.15982 | 79,962,300 | +256 | +35.96.6.0/24 |
| 2024&#8209;10&#8209;31&nbsp;20:43:07 | 2.15982 | 79,962,044 | +40 | +3.4.15.112/28,&nbsp;+3.4.15.128/28,&nbsp;+3.4.12.40/30,&nbsp;... |
| 2024&#8209;10&#8209;30&nbsp;18:33:08 | 2.15982 | 79,962,004 | -512 | -192.157.36.0/23 |
| 2024&#8209;10&#8209;30&nbsp;17:03:17 | 2.15983 | 79,962,516 | +512 | +16.15.14.0/23 |
| 2024&#8209;10&#8209;29&nbsp;20:03:09 | 2.15982 | 79,962,004 | +512 | +35.96.4.0/23 |
| 2024&#8209;10&#8209;28&nbsp;16:13:09 | 2.15980 | 79,961,492 | +512 | +192.157.36.0/23 |
| 2024&#8209;10&#8209;28&nbsp;14:43:13 | 2.15979 | 79,960,980 | -32,512 | +192.189.197.0/24,&nbsp;-16.64.128.0/17 |
| 2024&#8209;10&#8209;25&nbsp;02:13:11 | 2.16067 | 79,993,492 | -512 | -192.157.36.0/23 |
| 2024&#8209;10&#8209;25&nbsp;00:53:09 | 2.16068 | 79,994,004 | +512 | +16.15.12.0/23 |


# 15 largest changes to date:

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2021&#8209;08&#8209;12&nbsp;18:31:15 | 1.75915 | 65,128,214 | +5,505,024 | +3.48.0.0/12,&nbsp;+35.96.0.0/12,&nbsp;+3.152.0.0/13,&nbsp;... |
| 2022&#8209;08&#8209;31&nbsp;20:33:06 | 1.93002 | 71,454,285 | +4,718,592 | +98.80.0.0/12,&nbsp;+184.32.0.0/12,&nbsp;+13.184.0.0/13,&nbsp;... |
| 2020&#8209;08&#8209;11&nbsp;16:19:14 | 1.50480 | 55,711,498 | +4,194,304 | +252.0.0.0/10 |
| 2020&#8209;08&#8209;12&nbsp;19:21:14 | 1.39151 | 51,517,198 | -4,194,304 | -252.0.0.0/10 |
| 2022&#8209;09&#8209;29&nbsp;20:23:06 | 1.89058 | 69,994,058 | -3,932,160 | -3.48.0.0/12,&nbsp;-35.96.0.0/12,&nbsp;-3.240.0.0/13,&nbsp;... |
| 2017&#8209;06&#8209;29&nbsp;22:42:11 | 0.74955 | 27,750,448 | +3,429,728 | +13.232.0.0/13,&nbsp;+34.240.0.0/13,&nbsp;+35.168.0.0/13,&nbsp;... |
| 2019&#8209;08&#8209;01&nbsp;20:03:05 | 1.24953 | 46,260,706 | +3,145,728 | +44.192.0.0/10,&nbsp;-3.192.0.0/12 |
| 2017&#8209;04&#8209;07&nbsp;18:22:10 | 0.65692 | 24,320,720 | +3,025,152 | +34.208.0.0/12,&nbsp;+34.224.0.0/12,&nbsp;+13.58.0.0/15,&nbsp;... |
| 2022&#8209;10&#8209;11&nbsp;22:43:07 | 1.96491 | 72,746,202 | +2,752,512 | +51.24.0.0/13,&nbsp;+57.104.0.0/13,&nbsp;+51.20.0.0/14,&nbsp;... |
| 2024&#8209;01&#8209;23&nbsp;21:43:07 | 2.10814 | 78,048,717 | +2,359,552 | +56.48.0.0/13,&nbsp;+16.28.0.0/14,&nbsp;+16.64.0.0/14,&nbsp;... |
| 2018&#8209;12&#8209;18&nbsp;21:54:17 | 1.05392 | 39,019,010 | +2,228,224 | +3.208.0.0/12,&nbsp;+3.224.0.0/12,&nbsp;+13.48.0.0/15 |
| 2016&#8209;04&#8209;22&nbsp;18:22:20 | 0.46701 | 17,290,016 | +2,214,656 | +52.200.0.0/13,&nbsp;+52.208.0.0/13,&nbsp;+52.36.0.0/14,&nbsp;... |
| 2022&#8209;10&#8209;12&nbsp;21:13:09 | 1.91535 | 70,911,194 | -1,835,008 | -13.192.0.0/13,&nbsp;-16.28.0.0/14,&nbsp;-40.172.0.0/14,&nbsp;... |
| 2017&#8209;12&#8209;21&nbsp;20:12:10 | 0.81440 | 30,151,184 | +1,703,936 | +18.208.0.0/13,&nbsp;+18.204.0.0/14,&nbsp;+18.224.0.0/14,&nbsp;... |
| 2024&#8209;01&#8209;23&nbsp;20:43:07 | 2.04441 | 75,689,165 | +1,572,864 | +56.68.0.0/14,&nbsp;+56.128.0.0/14,&nbsp;+56.136.0.0/14,&nbsp;... |
