import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b and b != c and a != c:
        print("Scalene")
    elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        print("Isosceles")

# gemini's feedback

import sys

while True:
    # 1. Read into a list directly
    sides = list(map(int, sys.stdin.readline().split()))

    # 2. Exit condition
    if sides[0] == 0:
        break

    # 3. Sort the list to easily find the max side
    # [10, 2, 5] -> becomes [2, 5, 10]
    sides.sort()

    # 4. Check Invalid: Largest side vs Sum of other two
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")

    # 5. Check types using Set (removes duplicates)
    # Length 1: {60} -> Equilateral
    # Length 2: {50, 40} -> Isosceles
    # Length 3: {3, 4, 5} -> Scalene
    elif len(set(sides)) == 1:
        print("Equilateral")
    elif len(set(sides)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
