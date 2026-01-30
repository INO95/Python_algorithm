# import sys

# n = int(sys.stdin.readline())
# numbers_n = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# numbers_m = list(map(int, sys.stdin.readline().split()))
# answer = [0 for i in range(m)]
# for i in range(n):
#     for j in range(m):
#         if numbers_n[i] == numbers_m[j]:
#             answer[j] = 1

# for x in answer:
#     print(x, end=" ")

# timeover

# import sys

# n = int(sys.stdin.readline())
# numbers_n = list(map(int, sys.stdin.readline().split()))
# numbers_n_dict = {num: i for i, num in enumerate(numbers_n)}

# m = int(sys.stdin.readline())
# numbers_m = list(map(int, sys.stdin.readline().split()))

# for i in range(m):
#     if numbers_n_dict.get(numbers_m[i]):
#         print(1, end=" ")
#     else:
#         if i == m - 1:
#             print(0)
#         else:
#             print(0, end=" ")

# fail
# gemini's help

import sys

# 1. Input N
n = int(sys.stdin.readline())

# 2. Use a SET for O(1) lookups.
#    We don't need the index, so set is better than dict.
cards = set(map(int, sys.stdin.readline().split()))

# 3. Input M
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

# 4. Check each number
for check in checks:
    # 'in' operator on a set is O(1) (Instant)
    if check in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
