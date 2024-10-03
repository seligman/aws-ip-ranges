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

[Comparing to other providers](https://github.com/seligman/cloud_sizes), as of 2024-10-03:

| | IPs | Percent |
| --- | ---: | ---: |
| Amazon AWS | 79,963,473 | 2.15986 |
| Microsoft Azure | 43,959,624 | 1.18737 |
| Google Cloud | 13,318,912 | 0.35975 |


# Last 15 updates:

(Changes that do not impact the counts are not shown)

| | Percent | IPs | Change | CIDRs |
| :--- | ---: | ---: | ---: | :--- |
| 2024&#8209;10&#8209;02&nbsp;19:43:09 | 2.15986 | 79,963,473 | +768 | +16.12.82.0/23,&nbsp;+16.12.81.0/24 |
| 2024&#8209;10&#8209;02&nbsp;16:13:17 | 2.15984 | 79,962,705 | +40,960 | +5.60.224.0/19,&nbsp;+5.60.208.0/20,&nbsp;+5.60.152.0/21,&nbsp;... |
| 2024&#8209;09&#8209;30&nbsp;23:43:10 | | | | Region mx-central-1 |
| 2024&#8209;09&#8209;30&nbsp;23:43:10 | | | | Region ap-southeast-7 |
| 2024&#8209;09&#8209;30&nbsp;23:43:10 | | | | Region ap-east-2 |
| 2024&#8209;09&#8209;30&nbsp;23:43:10 | 2.15873 | 79,921,745 | +821,809 | +43.208.0.0/13,&nbsp;+78.12.0.0/14,&nbsp;+15.190.96.0/19,&nbsp;... |
| 2024&#8209;09&#8209;27&nbsp;18:53:07 | 2.13653 | 79,099,936 | -256 | -52.129.225.0/24 |
| 2024&#8209;09&#8209;27&nbsp;16:53:09 | 2.13654 | 79,100,192 | +524,800 | +13.216.0.0/13,&nbsp;+43.193.64.0/24,&nbsp;+52.129.225.0/24 |
| 2024&#8209;09&#8209;24&nbsp;21:23:08 | 2.12236 | 78,575,392 | +8,192 | +93.77.128.0/19 |
| 2024&#8209;09&#8209;17&nbsp;20:03:08 | 2.12214 | 78,567,200 | +16,384 | +75.3.128.0/18 |
| 2024&#8209;09&#8209;17&nbsp;18:33:07 | 2.12170 | 78,550,816 | +16,384 | +75.3.0.0/18 |
| 2024&#8209;09&#8209;16&nbsp;21:33:10 | 2.12126 | 78,534,432 | +15,360 | +161.188.64.0/19,&nbsp;+161.188.48.0/20,&nbsp;+161.188.112.0/21,&nbsp;... |
| 2024&#8209;09&#8209;16&nbsp;20:13:07 | 2.12084 | 78,519,072 | +768 | +23.254.14.0/23,&nbsp;+23.254.13.0/24 |
| 2024&#8209;09&#8209;16&nbsp;00:13:10 | 2.12082 | 78,518,304 | +256 | +3.2.57.0/24 |
| 2024&#8209;09&#8209;12&nbsp;17:43:17 | 2.12081 | 78,518,048 | +1,280 | +23.254.8.0/22,&nbsp;+23.254.12.0/24 |


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
