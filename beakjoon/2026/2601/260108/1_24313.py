# import sys

# a, b = map(int, sys.stdin.readline().split())
# c = int(sys.stdin.readline())
# d = int(sys.stdin.readline())

# def func1(n):
#     return a * n + b

# if func1()

# 못 풀겠어서 gemini에게 요청
import sys

# 1. Read inputs
# First line: a1 and a0 for f(n) = a1*n + a0
a1, a0 = map(int, sys.stdin.readline().split())

# Second line: c for g(n) = c*n
c = int(sys.stdin.readline())

# Third line: n0 (start point)
n0 = int(sys.stdin.readline())

# 2. Check the two necessary conditions
# Condition A: The formula must be true at the starting point n0
start_condition = (a1 * n0 + a0) <= (c * n0)

# Condition B: The slope a1 must be <= c to prevent crossing later
slope_condition = a1 <= c

# 3. Print result
# Both conditions must be True
if start_condition and slope_condition:
    print(1)
else:
    print(0)
