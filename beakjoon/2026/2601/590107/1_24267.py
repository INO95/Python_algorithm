import sys

n = int(sys.stdin.readline())

# count = 0

# for i in range(1, n - 1):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n + 1):
#             count = count + 1

print(n * (n - 1) * (n - 2) // 6)
print(3)
