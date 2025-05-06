import sys

n = int(sys.stdin.readline().rstrip())

list = list(map(int, sys.stdin.readline().split()))

big = list[0]
small = list[0]

for i in range(len(list)):
    if list[i] > big:
        big = list[i]
    if list[i] < small:
        small = list[i]

print(f"{small} {big}")
