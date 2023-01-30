import string
str = '172.0.13.20'
str2 = '2020:0bc3:0:0:853e:0777:1234'


def check_ip_v4(ipv4) -> str:
    # .을 기준으로 분리
    ipnums = ipv4.split('.')

    # 분리한 문자별로 검사한다.
    for num in ipnums:
        # 길이가 0이거나 3보다 크면 neither
        if len(num) == 0 or len(num) > 3:
            return 'Neither'

        # 길이가 1이면서 0이어야 한다 혹은
        # isdigit() 문자열이 숫자로만 이루어져있는지 판단 : 숫자로만 이루어지면 true
        # 분리된 숫자 문자열이 255 미만이어야 함
        if (len(num) != 1 and num[0] == '0') or \
                not num.isdigit() or int(num) > 255:
            return 'Neither'
    # 모두 해당되지 않으면 IPv4
    return 'IPv4'


def check_ip_v6(ipv6) -> str:
    # : 기준으로 분리
    ipnums = ipv6.split(':')

    for num in ipnums:
        # 길이가 0이거나
        # 길이가 5 이상이거나
        # 16진수 요소에 속하지 않은 요소를 지니고 있다면 neither
        if len(num) == 0 or len(num) > 4 or \
                not all(c in string.hexdigits for c in num):
            return 'Neither'
    # 모두 해당되지 않으면 IPv6
    return 'IPv6'


# count() : 인자로 받은 값이 몇 번 나오는지 카운트
# . 혹은 : 이 몇 번 나오는지 카운트한다.
def validIpAdress(IP) -> str:
    if IP.count('.') == 3:
        return check_ip_v4(IP)
    elif IP.count(':') == 6:
        return check_ip_v6(IP)

    return 'Neither'


print(validIpAdress(str2))
