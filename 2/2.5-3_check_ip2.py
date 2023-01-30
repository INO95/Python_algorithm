import re
str = '172.0.13.20'
str2 = '2020:0bc3:0:0:853e:0777:1234'


def validIPAdress(IP: str) -> str:
    IPV4 = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'

    ipv4 = \
        re.compile(r'^({p}\.){{3}}{p}$'.format(p=IPV4))

    if ipv4.match(IP):
        return "IPv4"

    IPV6 = '([0-9a-f]{1,4})'

    ipv6 = \
        re.compile(r'^({p}\:){{6}}{p}$'.format(p=IPV6), re.IGNORECASE)

    if ipv6.match(IP):
        return "IPv6"

    return "Neither"


print(validIPAdress(str2))
