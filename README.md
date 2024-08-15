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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2024-08-15:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 78,676,000 | 2.12508 |
| Microsoft Azure | 42,330,340 | 1.14337 |
| Google Cloud | 13,075,200 | 0.35317 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2024&#8209;08&#8209;14&nbsp;15:43:16 | 2.12508 | 78,676,000 | +49,152 | +3.173.0.0/17,&nbsp;+3.172.64.0/18 |
| 2024&#8209;08&#8209;12&nbsp;18:53:10 | 2.12375 | 78,626,848 | +512 | +136.18.142.0/23 |
| 2024&#8209;08&#8209;10&nbsp;00:53:10 | 2.12374 | 78,626,336 | +512 | +35.71.123.0/24,&nbsp;+35.71.124.0/24 |
| 2024&#8209;08&#8209;09&nbsp;23:33:10 | 2.12373 | 78,625,824 | +256 | +35.71.122.0/24 |
| 2024&#8209;08&#8209;06&nbsp;23:53:09 | 2.12372 | 78,625,568 | +256 | +35.96.2.0/24 |
| 2024&#8209;08&#8209;06&nbsp;21:53:09 | 2.12371 | 78,625,312 | +256 | +35.96.1.0/24 |
| 2024&#8209;08&#8209;06&nbsp;16:43:07 | 2.12371 | 78,625,056 | -256 | -35.96.1.0/24 |
| 2024&#8209;07&#8209;26&nbsp;23:53:08 | 2.12371 | 78,625,312 | -256 | -3.4.11.0/24 |
| 2024&#8209;07&#8209;25&nbsp;21:43:09 | 2.12372 | 78,625,568 | +16 | +3.4.15.0/28 |
| 2024&#8209;07&#8209;24&nbsp;22:53:09 | 2.12372 | 78,625,552 | -866 | -13.34.0.128/26,&nbsp;-13.34.4.64/26,&nbsp;-13.34.4.192/26,&nbsp;... |
| 2024&#8209;07&#8209;24&nbsp;21:33:10 | 2.12374 | 78,626,418 | -1,137 | -13.34.16.128/25,&nbsp;-13.34.18.128/25,&nbsp;-13.34.14.192/26,&nbsp;... |
| 2024&#8209;07&#8209;24&nbsp;20:53:09 | 2.12377 | 78,627,555 | -1,852 | -13.34.35.0/24,&nbsp;-13.34.37.0/24,&nbsp;-13.34.27.0/25,&nbsp;... |
| 2024&#8209;07&#8209;24&nbsp;19:33:09 | 2.12382 | 78,629,407 | -1,032 | -13.34.41.0/24,&nbsp;-13.34.45.0/24,&nbsp;-13.34.46.128/25,&nbsp;... |
| 2024&#8209;07&#8209;24&nbsp;18:53:10 | 2.12385 | 78,630,439 | -1,780 | -13.34.65.0/24,&nbsp;-13.34.51.128/25,&nbsp;-13.34.52.128/25,&nbsp;... |
| 2024&#8209;07&#8209;24&nbsp;17:33:10 | 2.12390 | 78,632,219 | -778 | -13.34.74.0/25,&nbsp;-13.34.71.192/26,&nbsp;-13.34.72.64/26,&nbsp;... |


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
