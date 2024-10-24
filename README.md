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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2024-10-25:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 79,993,492 | 2.16067 |
| Microsoft Azure | 44,411,970 | 1.19959 |
| Google Cloud | 14,496,000 | 0.39154 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2024&#8209;10&#8209;24&nbsp;22:43:11 | 2.16067 | 79,993,492 | +20 | +3.4.15.96/28,&nbsp;+3.4.12.36/31,&nbsp;+3.4.12.35/32,&nbsp;... |
| 2024&#8209;10&#8209;24&nbsp;20:33:09 | 2.16067 | 79,993,472 | +256 | +15.248.140.0/24 |
| 2024&#8209;10&#8209;21&nbsp;20:53:11 | 2.16066 | 79,993,216 | +4,096 | +18.97.64.0/20 |
| 2024&#8209;10&#8209;21&nbsp;18:53:10 | 2.16055 | 79,989,120 | +131,072 | +13.134.0.0/15 |
| 2024&#8209;10&#8209;18&nbsp;23:03:11 | 2.15701 | 79,858,048 | +256 | +35.96.3.0/24 |
| 2024&#8209;10&#8209;18&nbsp;21:33:17 | 2.15700 | 79,857,792 | +16,384 | +75.2.128.0/18 |
| 2024&#8209;10&#8209;18&nbsp;20:53:08 | 2.15656 | 79,841,408 | +256 | +192.157.37.0/24 |
| 2024&#8209;10&#8209;18&nbsp;16:03:07 | 2.15655 | 79,841,152 | +256 | +192.157.36.0/24 |
| 2024&#8209;10&#8209;17&nbsp;19:33:10 | 2.15655 | 79,840,896 | +512 | +52.129.210.0/23 |
| 2024&#8209;10&#8209;16&nbsp;20:53:08 | 2.15653 | 79,840,384 | +33,280 | +56.68.0.0/17,&nbsp;+52.129.208.0/23 |
| 2024&#8209;10&#8209;16&nbsp;19:23:08 | 2.15563 | 79,807,104 | -65,536 | -56.68.0.0/16 |
| 2024&#8209;10&#8209;15&nbsp;23:53:10 | 2.15740 | 79,872,640 | +256 | +15.177.105.0/24 |
| 2024&#8209;10&#8209;15&nbsp;21:13:12 | 2.15740 | 79,872,384 | +256 | +142.4.165.0/24 |
| 2024&#8209;10&#8209;14&nbsp;16:13:11 | 2.15739 | 79,872,128 | +4,096 | +15.221.176.0/20 |
| 2024&#8209;10&#8209;11&nbsp;21:13:07 | 2.15728 | 79,868,032 | +256 | +142.4.164.0/24 |


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
