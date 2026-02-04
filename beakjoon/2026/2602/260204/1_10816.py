import sys

n = int(sys.stdin.readline())

numbers = {}

number_have = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    num = number_have[i]
    if num in numbers:
        numbers[num] = numbers[num] + 1
    else:
        numbers[num] = 1

m = int(sys.stdin.readline())
number_find = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    num = number_find[i]
    if num in numbers:
        print(numbers[num], end=" ")
    else:
        print(0, end=" ")