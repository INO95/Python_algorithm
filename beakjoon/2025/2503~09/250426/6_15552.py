import sys

T = int(sys.stdin.readline().rstrip())
arr = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append(a + b)

for i in range(len(arr)):
    print(arr[i])
