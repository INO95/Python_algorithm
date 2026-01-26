import sys

n = int(sys.stdin.readline())

numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# numbers.sort(key=lambda x: x[1])
# gemini's help
numbers.sort(key=lambda x: (x[1], x[0]))

for x, y in numbers:
    print(x, y)
