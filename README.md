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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2026-01-28:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 101,412,507 | 2.73921 |
| Microsoft Azure | 48,871,766 | 1.32005 |
| Google Cloud | 16,373,920 | 0.44227 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2026&#8209;01&#8209;27&nbsp;22:38:04 | 2.73921 | 101,412,507 | +1,024 | +18.96.4.0/22 |
| 2026&#8209;01&#8209;27&nbsp;19:18:04 | 2.73918 | 101,411,483 | +256 | +35.97.194.0/24 |
| 2026&#8209;01&#8209;27&nbsp;11:48:04 | 2.73917 | 101,411,227 | +256 | +15.248.161.0/24 |
| 2026&#8209;01&#8209;27&nbsp;08:28:04 | 2.73917 | 101,410,971 | +256 | +15.248.160.0/24 |
| 2026&#8209;01&#8209;27&nbsp;01:48:04 | 2.73916 | 101,410,715 | +2,816 | +15.193.56.0/21,&nbsp;+15.193.38.0/23,&nbsp;+15.193.37.0/24 |
| 2026&#8209;01&#8209;27&nbsp;00:08:04 | 2.73908 | 101,407,899 | +272 | +15.129.28.0/24,&nbsp;+69.107.12.16/28 |
| 2026&#8209;01&#8209;26&nbsp;21:38:04 | 2.73907 | 101,407,627 | +256 | +35.97.193.0/24 |
| 2026&#8209;01&#8209;26&nbsp;19:58:04 | 2.73907 | 101,407,371 | +256 | +35.97.131.0/24 |
| 2026&#8209;01&#8209;26&nbsp;16:38:04 | 2.73906 | 101,407,115 | +720,896 | +54.8.0.0/16,&nbsp;+54.102.0.0/16,&nbsp;+56.1.0.0/16,&nbsp;... |
| 2026&#8209;01&#8209;26&nbsp;14:58:04 | 2.71959 | 100,686,219 | +196,608 | +54.5.0.0/16,&nbsp;+56.47.0.0/16,&nbsp;+56.61.0.0/16 |
| 2026&#8209;01&#8209;24&nbsp;01:38:04 | 2.71428 | 100,489,611 | +262,144 | +40.32.0.0/16,&nbsp;+40.35.0.0/16,&nbsp;+40.188.0.0/16,&nbsp;... |
| 2026&#8209;01&#8209;23&nbsp;23:08:04 | 2.70720 | 100,227,467 | +655,360 | +184.76.0.0/14,&nbsp;+15.227.0.0/16,&nbsp;+15.249.0.0/16,&nbsp;... |
| 2026&#8209;01&#8209;23&nbsp;19:48:04 | 2.68950 | 99,572,107 | +1,310,976 | +184.208.0.0/12,&nbsp;+15.148.0.0/16,&nbsp;+15.159.0.0/16,&nbsp;... |
| 2026&#8209;01&#8209;23&nbsp;17:58:05 | 2.65409 | 98,261,131 | +1,441,792 | +184.192.0.0/12,&nbsp;+65.176.0.0/14,&nbsp;+51.172.0.0/15 |
| 2026&#8209;01&#8209;22&nbsp;21:38:05 | 2.61514 | 96,819,339 | +458,752 | +76.162.0.0/15,&nbsp;+83.162.0.0/15,&nbsp;+86.112.0.0/15,&nbsp;... |


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

If you find this project useful, consider [buying me a cup coffee](https://coff.ee/seligman).  Thanks!
