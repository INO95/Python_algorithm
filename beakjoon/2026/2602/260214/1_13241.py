import sys
input = sys.stdin.readline

# 최대공약수를 구함 (두 수를 모두 나눌 수 있는 수)
def gcd(a, b):
    # b가 0이 될 때 까지
    while b:
        # a에 b를 담고 b에 a에서 b를 나눈 나머지를 담음
        a, b = b, a % b
        # 유클리드 호재법이라고 함
    return a

out = []

a, b = map(int, input().split())
g = gcd(a, b)
out.append(str(a // g * b))

print("\n".join(out))


# (gpt) more simplely

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(a // gcd(a, b) * b)
