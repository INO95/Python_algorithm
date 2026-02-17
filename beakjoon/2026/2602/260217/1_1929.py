import sys, math

input = sys.stdin.readline

m, n = map(int, input().split())

def is_prime(n: int) -> bool:
    # 0, 1은 소수 아님
    if n < 2:
        return False
    # 2, 3은 소수
    if n < 4:
        return True
    # 2로 나누어 떨어지면 소수 아님
    if n % 2 == 0:
        return False

    r = int(math.isqrt(n))
    # 홀수만 검사 (3, 5, 7, ...)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if is_prime(i):
        print(i)


# 지피티 피드백

import sys, math
input = sys.stdin.readline

m, n = map(int, input().split())

is_prime = bytearray(b"\x01") * (n + 1)
if n >= 0: is_prime[0] = 0
if n >= 1: is_prime[1] = 0

for p in range(2, math.isqrt(n) + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:n+1:p] = b"\x00" * (((n - start) // p) + 1)

out = []
for x in range(max(2, m), n + 1):
    if is_prime[x]:
        out.append(str(x))

sys.stdout.write("\n".join(out))
