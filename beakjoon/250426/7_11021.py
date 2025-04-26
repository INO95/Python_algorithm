import sys

t = int(sys.stdin.readline().rstrip())
arr = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append(a + b)

for i in range(len(arr)):
    print("Case #" + (i + 1) + ": " + arr[i])
