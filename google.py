#!/usr/bin/env python3

import aws_ipv4_size
from netaddr import IPSet, IPNetwork
from requests import get

def main():
    # I'm shocked, shocked I tell you to see that MS requires you do
    # something oddball like dig into an HTML page to get the latest
    # data file.
    # Google publishes the list in a simple JSON file, and also in an
    # overly complex DNS TXT record, because of course they do
    url = "https://www.gstatic.com/ipranges/cloud.json"
    data = get(url).json()

    # Pull out all of the IPs, ignore IPv6
    google = IPSet(IPNetwork(y['ipv4Prefix']) for y in data['prefixes'] if 'ipv4Prefix' in y)

    # And produce the stats
    public, _internet, google = aws_ipv4_size.parse_aws(google)
    print(f'Google: {google:10d} {google / public * 100.0:6.2f}%')


if __name__ == "__main__":
    main()
