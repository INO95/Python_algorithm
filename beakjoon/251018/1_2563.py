import sys

coordinate = {}
for i in range(1, 101):
    for j in range(1, 101):
        coordinate[(i, j)] = False

cnt = int(sys.stdin.readline().rstrip())

squares = []
for _ in range(cnt):
    x, y = map(int, sys.stdin.readline().split())
    squares.append({x, y})
    for i in range(10):
        for j in range(10):
            coordinate[(x + i, y + j)] = True

extent = 0
for key, value in coordinate.items():
    if value == True:
        extent += 1
print(extent)

# 제미나이 제안 1

import sys

# 101x101 크기의 0으로 채워진 2차원 리스트 생성 (인덱스를 1부터 100까지 쓰기 위해)
paper = [[0] * 101 for _ in range(101)]

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # 색종이가 덮는 영역을 1로 표시
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[j][i] = 1

# 각 행의 합계를 모두 더하면 총 넓이가 됨
total_area = sum(sum(row) for row in paper)
print(total_area)

# 제미나이 제안 2

import sys

# 101x101 크기의 0으로 채워진 2차원 리스트 생성 (인덱스를 1부터 100까지 쓰기 위해)
paper = [[0] * 101 for _ in range(101)]

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # 색종이가 덮는 영역을 1로 표시
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[j][i] = 1

# 각 행의 합계를 모두 더하면 총 넓이가 됨
total_area = sum(sum(row) for row in paper)
print(total_area)
