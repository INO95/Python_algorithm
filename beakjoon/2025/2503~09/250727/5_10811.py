import sys

n, m = map(int, sys.stdin.readline().split())

baskets = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp_num = j - i + 1
    temp_baskets = []
    temp_i = i
    for index in range(temp_num):
        temp_baskets.append(baskets[temp_i - 1])
        temp_i = temp_i + 1
    temp_baskets.reverse()
    for index in range(temp_num):
        baskets[i - 1] = temp_baskets[index]
        i = i + 1
        index = index + 1

print(*baskets)

# gemini가 개선한 코드

# import sys

# n, m = map(int, sys.stdin.readline().split())

# baskets = list(range(1, n + 1))

# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     # i-1부터 j까지의 슬라이스를 뒤집어서 다시 그 위치에 할당
#     baskets[i-1:j] = baskets[i-1:j][::-1]

# print(*baskets)
