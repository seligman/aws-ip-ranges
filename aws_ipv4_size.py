#!/usr/bin/env python3

from netaddr import IPSet, IPNetwork
from urllib.request import urlopen
import json

def parse_aws(ip_ranges=None):
    if ip_ranges is None:
        # Get the current IP Ranges from AWS.
        # Fun fact: The minutes in "createDate" in this data file has 
        # almost 1/2 a chance of being 13, 43, or 59, and the seconds 
        # has almost 1/2 a chance of being 4, 10, or 11.  Well, I 
        # thought it was a fun fact.
        ip_ranges = json.loads(urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json").read())

    if isinstance(ip_ranges, IPSet):
        aws = ip_ranges
    else:
        # Merge everything from AWS into one IPSet.
        # This ignores IPv6, but so does everyone else.
        aws = IPSet([IPNetwork(x["ip_prefix"]) for x in ip_ranges["prefixes"]])

    # These are all of the IPv4 addresses, there are 2^32 of them.
    # IPSet used here just because I like the symmetry of it all.
    internet = IPSet()
    internet.add("0.0.0.0/0")

    # There are less than 2^32 IPv4 addresses that AWS could control.
    # There are ones not in this private list that they couldn't touch,
    # but it's a reasonable start.
    private = IPSet([IPNetwork(x) for x in [
        "0.0.0.0/8",       # RFC 1700 broadcast addresses
        "10.0.0.0/8",      # RFC 1918 Private address space (aka, your work LAN)
        "100.64.0.0/10",   # IANA Carrier Grade NAT (not your home NAT, no sirree)
        "100.64.0.0/10",   # RFC 6598 Carrier graded NAT
        "127.0.0.0/8",     # Loopback addresses (because you need 16 million IPs for localhost)
        "169.254.0.0/16",  # RFC 6890 Link Local address (aka, the broken LAN)
        "172.16.0.0/12",   # RFC 1918 Private address space (aka, Goldilocks' LAN)
        "192.0.0.0/24",    # RFC 5736 IANA IPv4 Special Purpose Address Registry
        "192.0.2.0/24",    # RFC 5737 TEST-NET for internal use
        "192.168.0.0/16",  # RFC 1918 Private address space (aka, your home LAN)
        "192.88.99.0/24",  # RFC 3068 6to4 anycast relays
        "198.18.0.0/15",   # RFC 2544 Testing of inter-network communications
        "198.51.100.0/24", # RFC 5737 TEST-NET-2 for internal use
        "203.0.113.0/24",  # RFC 5737 TEST-NET-3 for internal use
        "224.0.0.0/4",     # RFC 5771 Multicast Addresses
        "240.0.0.0/4",     # RFC 6890 Reserved for future use (or if the RFC team needs to make a few bucks)
    ]])

    # I hope you had fun on this little journey.

    public = internet.size - private.size
    internet = internet.size
    aws = aws.size

    return public, internet, aws


def main():
    public, internet, aws = parse_aws()

    print("-" * 50)
    print(f"Total IPv4 addresses:  {internet:10d}")
    print(f"Public IPv4 addresses: {public:10d} {public / internet * 100.0:10.6f}%")
    print(f"AWS IPv4 addresses:    {aws:10d} {aws / public * 100.0:10.6f}%")
    print("-" * 50)


if __name__ == "__main__":
    main()
