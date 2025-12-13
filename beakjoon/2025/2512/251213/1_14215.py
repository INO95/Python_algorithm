import sys

sides = list(map(int, sys.stdin.readline().split()))
sides.sort(reverse=True)

# 삼각형의 조건 : 한 변의 길이는
# 나머지 두 변의 길이의 합 보다 작아야 한다

if sides[0] < sides[1] + sides[2]:
    print(sides[0] + sides[1] + sides[2])
else:
    sides[0] = sides[1] + sides[2] - 1
    print(sides[0] + sides[1] + sides[2])

# gemini's feedback

import sys

# 1. Read and sort (I prefer ascending order usually, but descending is fine too!)
sides = sorted(list(map(int, sys.stdin.readline().split())))

# sides[0] is small, sides[1] is medium, sides[2] is large (because sorted ascending)
# If you keep reverse=True, then sides[0] is large. Let's stick to your logic (Descending).
sides.sort(reverse=True)

# sides[0] = max
# sides[1], sides[2] = others

if sides[0] < sides[1] + sides[2]:
    # Valid triangle: just print the sum
    print(sum(sides))
else:
    # Invalid: maximize the perimeter
    # The max perimeter is always (sum of two smaller sides) * 2 - 1
    print((sides[1] + sides[2]) * 2 - 1)
