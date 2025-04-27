import sys

for line in sys.stdin:
    if not line.rstrip():
        break
    a, b = map(int, line.rstrip().split())
    print(a + b)
