import sys

n = int(sys.stdin.readline())
dots = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
]
length = 2
addedLength = 1

# 밑변의 길이 2 3 5 9 17
# 늘어난 수 1 2 4 8 -> 2의 제곱만큼 누적해서 더해진다
# n = 1 -> 2의 0승 = 1 -> 원래 2에서 1 늘어나서 3
# n = 2 -> 2의 1승 = 2 -> 원래 3에서 2 늘어나서 5
# n = 3 -> 2의 2승 = 4 -> 원래 5에서 4 늘어나서 9
# n = 4 -> 2의 3승 = 8 -> 원래 9에서 8 늘어나서 17
if n == 1:
    length = length + addedLength
for _ in range(n - 1):
    addedLength = addedLength * 2
    length = length + addedLength
for i in range(length):
    for j in range(length):
        if dots.count([i, j]) == 0:
            dots.append([i, j])
print(len(dots))


# 풀이 자체는 맞는데 for문이 이중 for문이라서 시간초과로 뜬다... 제미나이의 답

import sys

n = int(sys.stdin.readline())

# 1. n번째 단계의 한 변의 점 개수를 구합니다.
# (2**n은 2의 n제곱)
side_dots = (2**n) + 1

# 2. 총 점의 개수는 (한 변의 점 개수)의 제곱입니다.
total_dots = side_dots**2

print(total_dots)
