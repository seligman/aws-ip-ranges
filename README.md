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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2026-05-16:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 101,727,578 | 2.74772 |
| Microsoft Azure | 49,685,703 | 1.34204 |
| Google Cloud | 16,871,040 | 0.45570 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2026&#8209;05&#8209;16&nbsp;04:57:05 | 2.74772 | 101,727,578 | +256 | +13.248.82.0/24 |
| 2026&#8209;05&#8209;15&nbsp;01:47:05 | 2.74771 | 101,727,322 | +2 | +104.255.56.49/32,&nbsp;+104.255.56.50/32 |
| 2026&#8209;05&#8209;14&nbsp;19:17:05 | 2.74771 | 101,727,320 | -256 | -23.228.247.0/24 |
| 2026&#8209;05&#8209;14&nbsp;05:07:06 | 2.74772 | 101,727,576 | +2,048 | +15.248.184.0/21 |
| 2026&#8209;05&#8209;12&nbsp;22:07:05 | 2.74766 | 101,725,528 | +2,560 | +136.18.168.0/21,&nbsp;+136.18.162.0/23 |
| 2026&#8209;05&#8209;12&nbsp;16:27:06 | 2.74759 | 101,722,968 | +1,024 | +1.178.180.0/22 |
| 2026&#8209;05&#8209;12&nbsp;03:07:06 | 2.74756 | 101,721,944 | +32 | +52.94.250.192/28,&nbsp;+76.223.170.144/28 |
| 2026&#8209;05&#8209;11&nbsp;17:07:05 | 2.74756 | 101,721,912 | +16,384 | +51.74.128.0/18 |
| 2026&#8209;05&#8209;08&nbsp;19:37:05 | 2.74712 | 101,705,528 | +136,192 | +46.168.0.0/15,&nbsp;+15.190.176.0/20,&nbsp;+15.190.224.0/22 |
| 2026&#8209;05&#8209;08&nbsp;17:17:06 | 2.74344 | 101,569,336 | +2,048 | +23.254.32.0/21 |
| 2026&#8209;05&#8209;08&nbsp;15:07:05 | 2.74339 | 101,567,288 | +256 | +23.228.247.0/24 |
| 2026&#8209;05&#8209;07&nbsp;23:27:06 | 2.74338 | 101,567,032 | +256 | +15.177.108.0/24 |
| 2026&#8209;05&#8209;07&nbsp;21:07:06 | 2.74337 | 101,566,776 | +16,384 | +51.74.192.0/18 |
| 2026&#8209;05&#8209;07&nbsp;01:17:04 | 2.74293 | 101,550,392 | +4,096 | +35.98.144.0/20 |
| 2026&#8209;05&#8209;06&nbsp;15:47:05 | 2.74282 | 101,546,296 | +4 | +15.248.162.2/31,&nbsp;+15.248.162.4/31 |


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
