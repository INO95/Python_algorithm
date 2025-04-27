import sys

isZeroZero = False
a = 0
b = 0

while not isZeroZero:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0:
        isZeroZero = True
    else:
        print(str(a + b))
