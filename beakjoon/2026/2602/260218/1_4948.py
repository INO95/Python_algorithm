# import sys, math
# input = sys.stdin.readline

# while True:

#     n = int(input())
#     if n == 0:
#         break
#     m = n * 2

#     is_prime = bytearray(b"\x01") * (m + 1)
#     if m >= 0: is_prime[0] = 0
#     if m >= 1: is_prime[1] = 0

#     for p in range(2, math.isqrt(m) + 1):
#         if is_prime[p]:
#             start = p * p
#             is_prime[start:m+1:p] = b"\x00" * (((m - start) // p) + 1)

#     out = []
#     for x in range(max(2, n + 1), m + 1):
#         if is_prime[x]:
#             out.append(str(x))

#     print(len(out))


# gpt 피드백

import sys, math
input = sys.stdin.readline

nums = []
while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)

if not nums:
    sys.exit()

max_n = max(nums)
limit = 2 * max_n

is_prime = bytearray(b"\x01") * (limit + 1)
is_prime[0] = is_prime[1] = 0

for p in range(2, math.isqrt(limit) + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:limit+1:p] = b"\x00" * (((limit - start) // p) + 1)

# (선택) 누적합으로 "구간 소수 개수"를 O(1)로 만들기
prefix = [0] * (limit + 1)
s = 0
for i in range(limit + 1):
    s += is_prime[i]
    prefix[i] = s

out = []
for n in nums:
    out.append(str(prefix[2*n] - prefix[n]))
sys.stdout.write("\n".join(out))
