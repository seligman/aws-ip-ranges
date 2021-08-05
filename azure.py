#!/usr/bin/env python3

import aws_ipv4_size
from netaddr import IPSet, IPNetwork
from itertools import chain
from requests import get
import re

def main():
    # I'm shocked, shocked I tell you to see that MS requires you do
    # something oddball like dig into an HTML page to get the latest
    # data file.
    url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"
    data = get(url).text
    m = re.search('(?P<json>https://download.*?\.json)', data)
    url = m.group("json")
    data = get(url).json()

    # Pull out all of the IPs
    azure = IPSet(IPNetwork(y) for y in chain.from_iterable(x['properties']['addressPrefixes'] for x in data['values']))
    # Ignore IPv6
    azure = azure & IPSet(IPNetwork("0.0.0.0/0"))

    # And produce the stats
    public, _internet, azure = aws_ipv4_size.parse_aws(azure)
    print(f'Azure: {azure:10d} {azure / public * 100.0:6.2f}%')


if __name__ == "__main__":
    main()
