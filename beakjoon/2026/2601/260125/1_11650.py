import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    numbers.append((x, y))
numbers.sort()
for i in range(n):
    print(numbers[i][0], numbers[i][1])

# gemini

import sys

# 1. Read N
n = int(sys.stdin.readline())

# 2. Read inputs into a list of tuples using List Comprehension
# This replaces the 3-line for loop for appending.
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 3. Sort
# Python automatically sorts by the first element (x),
# then the second element (y) if the first ones are equal.
numbers.sort()

# 4. Print results using Unpacking
# Instead of using numbers[i][0], we unpack x and y directly.
for x, y in numbers:
    print(x, y)
