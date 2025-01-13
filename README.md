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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2025-01-11:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 82,265,855 | 2.22205 |
| Microsoft Azure | 45,036,635 | 1.21646 |
| Google Cloud | 14,592,256 | 0.39414 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2025&#8209;01&#8209;13&nbsp;20:33:10 | 2.22205 | 82,265,855 | +256 | +35.96.0.0/24 |
| 2025&#8209;01&#8209;10&nbsp;19:13:10 | 2.22204 | 82,265,599 | -6,144 | -18.34.32.0/20,&nbsp;-18.34.240.0/22,&nbsp;-18.34.248.0/22 |
| 2025&#8209;01&#8209;10&nbsp;01:13:11 | 2.22220 | 82,271,743 | +256 | +35.96.15.0/24 |
| 2025&#8209;01&#8209;09&nbsp;01:13:11 | 2.22220 | 82,271,487 | +261 | +52.93.52.160/29,&nbsp;+52.93.53.0/29,&nbsp;+52.93.84.160/29,&nbsp;... |
| 2024&#8209;12&#8209;20&nbsp;23:03:10 | | | | Region me-west-1 |
| 2024&#8209;12&#8209;20&nbsp;23:03:10 | 2.22219 | 82,271,226 | +262,144 | +51.204.0.0/14 |
| 2024&#8209;12&#8209;19&nbsp;01:33:08 | 2.21511 | 82,009,082 | +256 | +35.96.14.0/24 |
| 2024&#8209;12&#8209;18&nbsp;23:33:08 | 2.21510 | 82,008,826 | -512 | -35.96.0.0/24,&nbsp;-35.96.10.0/24 |
| 2024&#8209;12&#8209;11&nbsp;20:53:09 | 2.21512 | 82,009,338 | +393,216 | +88.108.0.0/14,&nbsp;+13.150.0.0/15 |
| 2024&#8209;12&#8209;11&nbsp;19:33:07 | 2.20450 | 81,616,122 | +1,441,792 | +32.192.0.0/12,&nbsp;+51.200.0.0/14,&nbsp;+43.220.0.0/15 |
| 2024&#8209;12&#8209;09&nbsp;19:43:12 | 2.16555 | 80,174,330 | +256 | +206.72.209.0/24 |
| 2024&#8209;12&#8209;06&nbsp;22:43:09 | 2.16555 | 80,174,074 | +6,912 | +18.34.32.0/20,&nbsp;+18.34.240.0/22,&nbsp;+18.34.248.0/22,&nbsp;... |
| 2024&#8209;12&#8209;05&nbsp;19:13:07 | 2.16536 | 80,167,162 | +512 | +142.4.166.0/23 |
| 2024&#8209;12&#8209;05&nbsp;15:33:16 | 2.16534 | 80,166,650 | +256 | +136.18.2.0/24 |
| 2024&#8209;12&#8209;05&nbsp;14:03:09 | 2.16534 | 80,166,394 | +1,024 | +136.18.4.0/22 |


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
