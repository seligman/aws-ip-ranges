# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).
You can read more about the file [here](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
If you want to look up an IP address, you can see if it's from any of the cloud providers using [this tool](https://cloud-ips.s3-us-west-2.amazonaws.com/index.html).

This repository tracks changes to that file, and based off a trigger on the SNS 
topic automatically produces this chart showing how what percentage of the 
Internet's IPv4 address space AWS is in control of.  Here's some 
more [information about when different regions](announces.md) came 
online, and here's an [animation of the history](https://youtu.be/v__lzuvKxU0) 
of the AWS's IP usage.

To get updates as they happen:

[![RSS Icon (Full Feed)](images/rss_badge.svg)](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss.xml)
[![RSS Icon (Large Changes)](images/rss_badge_partial.svg)](https://raw.githubusercontent.com/seligman/aws-ip-ranges/master/rss_big_changes.xml)

![History of AWS](history_count.svg)

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2025-03-17:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 91,574,883 | 2.47349 |
| Microsoft Azure | 46,127,919 | 1.24594 |
| Google Cloud | 14,604,544 | 0.39448 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2025&#8209;03&#8209;17&nbsp;18:23:22 | 2.47349 | 91,574,883 | +256 | +15.248.143.0/24 |
| 2025&#8209;03&#8209;17&nbsp;15:23:17 | 2.47348 | 91,574,627 | +16,384 | +16.56.64.0/18 |
| 2025&#8209;03&#8209;13&nbsp;00:23:16 | 2.47304 | 91,558,243 | +1,792 | +16.15.16.0/22,&nbsp;+16.12.84.0/23,&nbsp;+16.12.86.0/24 |
| 2025&#8209;03&#8209;11&nbsp;18:23:20 | 2.47299 | 91,556,451 | +4,096 | +18.97.96.0/20 |
| 2025&#8209;03&#8209;11&nbsp;16:53:17 | 2.47288 | 91,552,355 | +4,096 | +18.97.80.0/20 |
| 2025&#8209;03&#8209;10&nbsp;19:53:18 | 2.47277 | 91,548,259 | +1,900,544 | +16.22.0.0/15,&nbsp;+16.48.0.0/15,&nbsp;+16.58.0.0/15,&nbsp;... |
| 2025&#8209;03&#8209;10&nbsp;18:23:19 | 2.42143 | 89,647,715 | +524,288 | +16.152.0.0/15,&nbsp;+16.164.0.0/15,&nbsp;+16.174.0.0/15,&nbsp;... |
| 2025&#8209;03&#8209;10&nbsp;16:53:20 | 2.40727 | 89,123,427 | +6,225,920 | +100.48.0.0/12,&nbsp;+16.144.0.0/13,&nbsp;+16.192.0.0/13,&nbsp;... |
| 2025&#8209;03&#8209;07&nbsp;16:53:21 | 2.23911 | 82,897,507 | -256 | -51.0.30.0/24 |
| 2025&#8209;02&#8209;28&nbsp;20:23:17 | 2.23911 | 82,897,763 | +131,328 | +15.103.0.0/16,&nbsp;+15.128.0.0/16,&nbsp;+35.96.248.0/24 |
| 2025&#8209;02&#8209;28&nbsp;11:53:16 | 2.23557 | 82,766,435 | +96 | +150.222.54.0/26,&nbsp;+150.222.54.64/27 |
| 2025&#8209;02&#8209;26&nbsp;20:13:16 | 2.23556 | 82,766,339 | +256 | +192.157.36.0/24 |
| 2025&#8209;02&#8209;26&nbsp;16:43:20 | 2.23556 | 82,766,083 | +65,536 | +13.160.0.0/16 |
| 2025&#8209;02&#8209;25&nbsp;23:13:18 | 2.23379 | 82,700,547 | -256 | -192.157.36.0/24 |
| 2025&#8209;02&#8209;25&nbsp;17:23:20 | 2.23379 | 82,700,803 | +131,072 | +13.152.0.0/16,&nbsp;+13.154.0.0/16 |


# 15 largest changes to date:

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2025&#8209;03&#8209;10&nbsp;16:53:20 | 2.40727 | 89,123,427 | +6,225,920 | +100.48.0.0/12,&nbsp;+16.144.0.0/13,&nbsp;+16.192.0.0/13,&nbsp;... |
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
| 2025&#8209;03&#8209;10&nbsp;19:53:18 | 2.47277 | 91,548,259 | +1,900,544 | +16.22.0.0/15,&nbsp;+16.48.0.0/15,&nbsp;+16.58.0.0/15,&nbsp;... |
| 2022&#8209;10&#8209;12&nbsp;21:13:09 | 1.91535 | 70,911,194 | -1,835,008 | -13.192.0.0/13,&nbsp;-16.28.0.0/14,&nbsp;-40.172.0.0/14,&nbsp;... |
