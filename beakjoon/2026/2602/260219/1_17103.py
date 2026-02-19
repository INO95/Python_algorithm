import sys
import math

input = sys.stdin.readline

t = int(input())
numbers = []
for _ in range(t):
    numbers.append(int(input()))

min_num = min(numbers)
max_num = max(numbers)

m = 2
n = max_num

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
        out.append(x)

for i in range(len(numbers)):
    cnt = 0
    j = 0
    while out[j] <= numbers[i] // 2:
        if is_prime[numbers[i] - out[j]]:
            cnt += 1
        j += 1
    print(cnt)


# 지피티 피드백

import sys, math
input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
max_num = max(numbers)

n = max_num
is_prime = bytearray(b"\x01") * (n + 1)
is_prime[0] = is_prime[1] = 0

for p in range(2, math.isqrt(n) + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:n+1:p] = b"\x00" * (((n - start) // p) + 1)

# 소수 리스트 만들기(반복용)
primes = [i for i in range(2, n + 1) if is_prime[i]]

out_lines = []
for num in numbers:
    cnt = 0
    half = num // 2
    for p in primes:
        if p > half:
            break
        if is_prime[num - p]:
            cnt += 1
    out_lines.append(str(cnt))

sys.stdout.write("\n".join(out_lines))
