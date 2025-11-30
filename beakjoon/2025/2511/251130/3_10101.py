import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a == b == c == 60:
    print("Equilateral")
elif a + b + c == 180:
    if a == b:
        print("Isosceles")
    elif b == c:
        print("Isosceles")
    elif a == c:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")
else:
    print("Error")

# refactored code 1

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b + c != 180:
    print("Error")
elif a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    # If sum is 180, and it's not Equilateral or Isosceles,
    # it MUST be Scalene. No math needed!
    print("Scalene")


# refactored code 2

import sys

angles = [int(sys.stdin.readline()) for _ in range(3)]

if sum(angles) != 180:
    print("Error")
elif len(set(angles)) == 1:
    print("Equilateral")
elif len(set(angles)) == 2:
    print("Isosceles")
else:
    print("Scalene")
