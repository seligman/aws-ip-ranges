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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2026-01-07:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 95,471,797 | 2.57874 |
| Microsoft Azure | 48,871,438 | 1.32004 |
| Google Cloud | 16,361,632 | 0.44194 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2026&#8209;01&#8209;07&nbsp;21:48:04 | 2.57874 | 95,471,797 | +256 | +1.178.18.0/24 |
| 2026&#8209;01&#8209;07&nbsp;20:08:04 | 2.57874 | 95,471,541 | +512 | +1.178.16.0/23 |
| 2026&#8209;01&#8209;07&nbsp;14:18:04 | 2.57872 | 95,471,029 | +8,192 | +51.0.136.0/21,&nbsp;+52.82.176.0/21,&nbsp;+54.222.32.0/21,&nbsp;... |
| 2026&#8209;01&#8209;07&nbsp;01:18:27 | 2.57850 | 95,462,837 | +256 | +1.178.103.0/24 |
| 2026&#8209;01&#8209;07&nbsp;00:18:28 | 2.57850 | 95,462,581 | +512 | +1.178.101.0/24,&nbsp;+1.178.102.0/24 |
| 2026&#8209;01&#8209;06&nbsp;22:18:27 | 2.57848 | 95,462,069 | +256 | +1.178.100.0/24 |
| 2026&#8209;01&#8209;06&nbsp;21:18:29 | 2.57848 | 95,461,813 | +256 | +1.178.95.0/24 |
| 2026&#8209;01&#8209;03&nbsp;07:18:24 | 2.57847 | 95,461,557 | +272 | +35.34.97.0/24,&nbsp;+69.107.11.48/28 |
| 2025&#8209;12&#8209;31&nbsp;05:18:24 | 2.57846 | 95,461,285 | +2 | +104.255.61.0/31 |
| 2025&#8209;12&#8209;30&nbsp;23:18:27 | 2.57846 | 95,461,283 | +256 | +35.97.192.0/24 |
| 2025&#8209;12&#8209;30&nbsp;21:18:23 | 2.57845 | 95,461,027 | +256 | +35.97.130.0/24 |
| 2025&#8209;12&#8209;25&nbsp;01:38:25 | 2.57845 | 95,460,771 | +256 | +40.168.224.0/24 |
| 2025&#8209;12&#8209;24&nbsp;01:18:27 | 2.57844 | 95,460,515 | -256 | -40.168.224.0/24 |
| 2025&#8209;12&#8209;23&nbsp;23:18:28 | 2.57845 | 95,460,771 | -256 | -40.168.225.0/24 |
| 2025&#8209;12&#8209;23&nbsp;00:48:29 | 2.57845 | 95,461,027 | +96 | +150.222.55.128/26,&nbsp;+150.222.55.96/27 |


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
