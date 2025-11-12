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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2025-11-13:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 95,558,831 | 2.58110 |
| Microsoft Azure | 48,479,246 | 1.30945 |
| Google Cloud | 16,311,968 | 0.44060 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2025&#8209;11&#8209;12&nbsp;23:08:41 | 2.58110 | 95,558,831 | +2,304 | +23.228.228.0/22,&nbsp;+23.228.232.0/22,&nbsp;+23.228.220.0/24 |
| 2025&#8209;11&#8209;12&nbsp;21:08:20 | 2.58103 | 95,556,527 | +1,280 | +35.111.128.0/22,&nbsp;+216.198.194.0/24 |
| 2025&#8209;11&#8209;12&nbsp;14:48:27 | 2.58100 | 95,555,247 | +256 | +122.200.61.0/24 |
| 2025&#8209;11&#8209;12&nbsp;00:08:30 | 2.58099 | 95,554,991 | +2,816 | +216.198.216.0/21,&nbsp;+216.244.38.0/23,&nbsp;+40.168.225.0/24 |
| 2025&#8209;11&#8209;11&nbsp;20:18:20 | 2.58092 | 95,552,175 | -512 | -43.226.24.0/23 |
| 2025&#8209;11&#8209;11&nbsp;18:38:20 | 2.58093 | 95,552,687 | +512 | +43.226.24.0/23 |
| 2025&#8209;11&#8209;11&nbsp;15:18:30 | 2.58092 | 95,552,175 | +16,384 | +149.128.64.0/18 |
| 2025&#8209;11&#8209;11&nbsp;04:28:20 | 2.58047 | 95,535,791 | +16 | +69.107.10.144/28 |
| 2025&#8209;11&#8209;11&nbsp;02:38:28 | 2.58047 | 95,535,775 | +256 | +40.168.225.0/24 |
| 2025&#8209;11&#8209;11&nbsp;00:38:24 | 2.58047 | 95,535,519 | +3,584 | +216.198.200.0/21,&nbsp;+216.198.196.0/22,&nbsp;+216.198.208.0/22,&nbsp;... |
| 2025&#8209;11&#8209;10&nbsp;21:18:24 | 2.58037 | 95,531,935 | +512 | +216.198.194.0/23 |
| 2025&#8209;11&#8209;10&nbsp;12:38:22 | 2.58036 | 95,531,423 | +4 | +104.255.57.172/30 |
| 2025&#8209;11&#8209;10&nbsp;10:38:19 | 2.58036 | 95,531,419 | +2 | +15.248.139.1/32,&nbsp;+15.248.139.2/32 |
| 2025&#8209;11&#8209;10&nbsp;02:28:19 | 2.58036 | 95,531,417 | +256 | +1.178.174.0/24 |
| 2025&#8209;11&#8209;08&nbsp;00:18:20 | 2.58035 | 95,531,161 | +256 | +40.168.224.0/24 |


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
