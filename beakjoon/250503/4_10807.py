import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

result = 0

for i in range(len(arr)):
    if m == arr[i]:
        result = result + 1

print(result)
