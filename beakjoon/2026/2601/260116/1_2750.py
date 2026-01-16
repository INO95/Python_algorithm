import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])

# gemini feedback
import sys

n = int(sys.stdin.readline())

# 1. Read input in one line
numbers = [int(sys.stdin.readline()) for _ in range(n)]

# 2. Sort
numbers.sort()

# 3. Print directly
for num in numbers:
    print(num)
