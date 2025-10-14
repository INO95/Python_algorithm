import sys

bigNum = -1  # 초기값을 -1로 변경 -> 초기값이 0이면 좌표 지정을 못해서 에러
x = 0
y = 0

for i in range(9):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(9):
        if bigNum < numbers[j]:
            bigNum = numbers[j]
            x = i + 1
            y = j + 1
print(bigNum)
print(x, y)

# 제미나이 제안

import sys

max_val = -1
max_row, max_col = 0, 0

for i in range(9):
    row_data = list(map(int, sys.stdin.readline().split()))
    # enumerate를 사용하여 현재 열의 인덱스(j)와 값(num)을 함께 가져옴
    for j, num in enumerate(row_data):
        if num > max_val:
            max_val = num
            max_row = i + 1  # 행 번호 (1-indexed)
            max_col = j + 1  # 열 번호 (1-indexed)

print(max_val)
print(max_row, max_col)
