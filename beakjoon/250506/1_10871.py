import sys

n, x = map(int, sys.stdin.readline().rstrip().split())

list = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(len(list)):
    if list[i] < x:
        result.append(list[i])

for i in range(len(result)):
    print(result[i], end=" ")
