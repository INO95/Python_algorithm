# import sys

# n = int(sys.stdin.readline())

# for i in range(n):
#     for _ in range(n - i - 1):
#         print(" ", end="")
#     for _ in range(2 * i + 1):
#         print("*", end="")
#     print()
# for i in range(n - 1):
#     for _ in range(i + 1):
#         print(" ", end="")
#     for _ in range(2 * (n - 1) - (2 * i + 1)):
#         print("*", end="")
#     print()

# 제미나이 제안 1

# import sys

# n = int(sys.stdin.readline())

# # 다이아몬드 위쪽 부분
# for i in range(1, n + 1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# # 다이아몬드 아래쪽 부분
# for i in range(n - 1, 0, -1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)


# 제미나이 제안 2

import sys

n = int(sys.stdin.readline())

# -n+1 부터 n-1 까지 반복
for i in range(-(n - 1), n):
    # i의 절댓값을 이용해 공백 개수를 계산
    spaces_count = abs(i)
    # 전체 너비(2*n-1)에서 공백을 뺀 만큼 별 개수를 계산
    stars_count = (2 * n - 1) - (2 * spaces_count)

    print(" " * spaces_count + "*" * stars_count)
