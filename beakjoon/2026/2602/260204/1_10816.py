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

# gemini's feedback

import sys
from collections import Counter

# 1. Input N
n = int(sys.stdin.readline())

# 2. Count cards immediately using Counter
#    This replaces the manual for-loop to build the dictionary.
cards = Counter(map(int, sys.stdin.readline().split()))

# 3. Input M
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

# 4. Print results
for target in targets:
    # Counter returns 0 automatically if the key is missing,
    # but regular dicts need .get(target, 0)
    print(cards[target], end=" ")