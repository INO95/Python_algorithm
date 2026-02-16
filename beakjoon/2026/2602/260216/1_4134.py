import sys
import math

input = sys.stdin.readline

n = int(input())

# 소수 범위 구하는 코드 인터넷에서 가져옴

def is_prime(n):
    if n < 2: return False  # 0, 1은 소수가 아님
    # 2부터 n의 제곱근까지 나눔 (효율적)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 나누어 떨어지면 소수가 아님
    return True

for _ in range(n):
    num = int(input())

    while True:
        if is_prime(num):
            print(num)
            break
        else:
            num += 1


#  gpt 팁

import sys
import math

input = sys.stdin.readline

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

t = int(input())
out = []

for _ in range(t):
    num = int(input())
    if num <= 2:
        out.append("2")
        continue
    # 2를 제외하면 짝수는 소수 불가 → 홀수부터 시작
    if num % 2 == 0:
        num += 1

    while not is_prime(num):
        num += 2  # 홀수만 계속 확인

    out.append(str(num))

print("\n".join(out))
