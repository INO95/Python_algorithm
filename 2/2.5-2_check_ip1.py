import string
str = '172.0.13.20'
str2 = '2020:0bc3:0:0:853e:0777:1234'


def check_ip_v4(ipv4) -> str:
    ipnums = ipv4.split('.')

    for num in ipnums:
        if len(num) == 0 or len(num) > 3:
            return 'Neither'

        if (len(num) != 1 and num[0] == '0') or \
                not num.isdigit() or int(num) > 255:
            return 'Neither'
    return 'IPv4'


def check_ip_v6(ipv6) -> str:
    ipnums = ipv6.split(':')

    for num in ipnums:
        if len(num) == 0 or len(num) > 4 or \
                not all(c in string.hexdigits for c in num):
            return 'Neither'
    return 'IPv6'


def validIpAdress(IP) -> str:
    if IP.count('.') == 3:
        return check_ip_v4(IP)
    elif IP.count(':') == 6:
        return check_ip_v6(IP)

    return 'Neither'


# 날ㅋ먹ㅋ
print(validIpAdress(str2))
