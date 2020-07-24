# AWS's ip-ranges.json

AWS provides a data file showing the current IP ranges their
services use, called [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json).  You 
can read more about the file [here](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).

This repository tracks changes to that file, and based off a trigger on the SNS topic 
automatically produces this chart showing how what percentage of the Internet's IPv4 
address space AWS is in control of.

![History of AWS](history_count.png)

# Last 10 updates:

| | Percent | IPs | Change |
| :--- | ---: | ---: | ---: |
| 2020-07-24 21:19:14 | 1.38235 | 51178239 | +65536 |
| 2020-07-24 20:39:13 | 1.38058 | 51112703 | +768 |
| 2020-07-24 20:19:14 | 1.38056 | 51111935 | +1024 |
| 2020-07-22 21:39:12 | 1.38053 | 51110911 | 0 |
| 2020-07-22 14:39:14 | 1.38053 | 51110911 | +4 |
| 2020-07-22 01:19:13 | 1.38053 | 51110907 | +30 |
| 2020-07-22 00:19:13 | 1.38053 | 51110877 | 0 |
| 2020-07-21 23:19:13 | 1.38053 | 51110877 | 0 |
| 2020-07-21 22:39:13 | 1.38053 | 51110877 | 0 |
| 2020-07-21 22:19:14 | 1.38053 | 51110877 | +256 |


# 10 largest changes to date:

| | Percent | IPs | Change |
| :--- | ---: | ---: | ---: |
| 2019-08-01 20:03:05 | 1.24953 | 46260706 | +3145728 |
| 2018-12-18 21:54:17 | 1.05392 | 39019010 | +2228224 |
| 2017-12-21 20:12:10 | 0.81440 | 30151184 | +1703936 |
| 2018-08-22 21:22:35 | 0.95738 | 35444840 | +1572864 |
| 2019-07-30 16:43:04 | 1.16456 | 43114908 | +1310720 |
| 2020-04-29 00:13:11 | 1.37105 | 50759849 | +1048576 |
| 2018-04-25 16:16:17 | 0.86887 | 32167704 | +917504 |
| 2019-10-28 01:03:09 | 1.28580 | 47603480 | +732413 |
| 2019-05-08 20:19:04 | 1.11038 | 41109242 | +655360 |
| 2019-07-18 21:23:05 | 1.12920 | 41805914 | +655224 |
