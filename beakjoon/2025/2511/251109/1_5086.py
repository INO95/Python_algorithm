import sys

switch = True
numbers = []
while switch:
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        switch = False
    else:
        if (y / x).is_integer():
            print("factor")
        elif (x / y).is_integer():
            print("multiple")
        else:
            print("neither")

# 맞았지만 제미나이가 제안한 더 나은 코드

import sys

while True:
    x, y = map(int, sys.stdin.readline().split())

    # 1. Exit condition is checked first
    if x == 0 and y == 0:
        break

    # 2. Logic using the modulo operator (%)
    if y % x == 0:
        print("factor")
    elif x % y == 0:
        print("multiple")
    else:
        print("neither")
