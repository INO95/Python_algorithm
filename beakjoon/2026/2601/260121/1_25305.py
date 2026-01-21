import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort(reverse=True)
print(numbers[k - 1])
