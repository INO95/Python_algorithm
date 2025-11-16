import sys
from collections import Counter

a, b, c = map(int, sys.stdin.readline().rstrip().split())

arr = [a, b, c]
sortedArr = sorted(set(arr), reverse=True)

if len(sortedArr) == 1:
    print(10000 + sortedArr[0] * 1000)
elif len(sortedArr) == 2:
    counter = Counter(arr)
    dup = [item for item, count in counter.items() if count > 1]
    print(1000 + dup[0] * 100)
else:
    print(sortedArr[0] * 100)
