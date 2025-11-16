import sys

a, b, v = map(int, sys.stdin.readline().split())
# dist = 0
# days = 1
# while True:
#     dist += a
#     if dist >= v:
#         break
#     dist -= b
#     days += 1
# print(days)
# -> 너무 오래걸림

# a - b = 하루에 올라가는 길이
distPerDay = a - b
if (v / distPerDay).is_integer():
    print(int(v / distPerDay) - b)
else:
    print(int(v / distPerDay) + 1)

# 제미니 답안

import sys

a, b, v = map(int, sys.stdin.readline().split())

# 1. 마지막 날을 제외하고 올라가야 할 높이
target = v - a
distPerDay = a - b

# 2. 'target'에 도달하는 데 며칠 걸리는지 계산
# (v-a)가 (a-b)로 나누어 떨어지는 경우
if target % distPerDay == 0:
    days_before_last = target // distPerDay
# (v-a)가 (a-b)로 나누어 떨어지지 않는 경우 (예: 9 / 4 = 2.25 -> 3일 필요)
else:
    days_before_last = (target // distPerDay) + 1

# 3. 마지막 날(+1)을 더해서 출력
print(days_before_last + 1)


import sys

a, b, v = map(int, sys.stdin.readline().split())

# (v - a) 높이를 (a - b)씩 오를 때 며칠 걸리는지 올림 계산
days_before_last = (v - a - 1) // (a - b) + 1

# 마지막 날 하루 더하기
print(days_before_last + 1)
