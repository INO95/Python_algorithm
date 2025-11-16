import sys

n, m = map(int, sys.stdin.readline().split())

baskets = []

for i in range(n):
    baskets.append(i + 1)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    num1 = baskets[i - 1]
    num2 = baskets[j - 1]
    baskets[i - 1] = num2
    baskets[j - 1] = num1

print(*baskets)

# gemini가 제안해준 개선된 코드

# import sys

# n, m = map(int, sys.stdin.readline().split())

# # 1부터 n까지의 숫자로 리스트 초기화 (개선점 1)
# baskets = list(range(1, n + 1))

# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     # 튜플을 이용해 두 위치의 값을 바로 교환 (개선점 2)
#     baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

# print(*baskets)
