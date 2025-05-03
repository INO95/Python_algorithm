import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())

hh = a
mm = b + c
if mm > 59:
    n = mm / 60
    hh += int(n)
    if hh > 23:
        hh = hh - 24
    mm = int(mm - int(n) * 60)

print(f"{hh} {mm}")
