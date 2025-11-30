import sys

n = int(sys.stdin.readline())

# 1 -> 4
# 2 -> 7
# 3 -> 12
# 4 -> 16
# 항상 맨 위의 사각형은 3의 길이를 가진다
# 가장 밑 사각형이 3개 이후에는 중간의 사각형들은 양쪽 각 1.5
# 가장 밑 사각형의 가장자리는 각 2.5
# 가장 밑 사각형의 갯수 (n - 2) * 1

# 가장 위 사각형의 길이는 3 고정
# 중간 양 사이드의 길이는 ((n - 2) * 3)
# ex) 가장 밑 사각형의 길이가 4면 (4 - 2) * 1.5 = 6
# 가장 밑 사이드의 길이는 5 고정
# 가장 밑 중간부의 길이는 (n - 2)
# ex) 가장 밑 사각형의 길이가 4면 (4 - 2) = 2

top = 0
middle_side = 0
bottom_side = 0
bottom_middle = 0

answer = 3 + ((n - 2) * 3) + 5 + (n - 2)
print(answer)

# the simple answer is 4n lol
