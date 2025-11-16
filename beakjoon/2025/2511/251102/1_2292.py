import sys

# 1 -> 1
# 2 -> 2~7
# 3 -> 8~19
# 4 -> 20~37
# 5 -> 38~61

# 2 8 20 38
#  6 12 18 24 30 36 ...

n = int(sys.stdin.readline().rstrip())

sum = 2
i = 0
while sum <= n:
    sum = sum + (6 * i)
    i = i + 1
if n == 1:
    print(1)
else:
    print(i)

# 제미나이 제안

import sys

n = int(sys.stdin.readline())

layer_max = 1  # 현재 레이어(껍질)의 최대 방 번호
layer_count = 1  # 현재 레이어(1부터 시작)

# n이 현재 레이어의 최대값보다 클 동안 반복
while n > layer_max:
    # 다음 레이어의 최대값을 계산
    # (6 * 1), (6 * 2), (6 * 3)... 만큼 더해짐
    layer_max += 6 * layer_count

    # 레이어를 1 증가
    layer_count += 1

print(layer_count)
