import sys

n, m = map(int, sys.stdin.readline().split())

card_list = list(map(int, sys.stdin.readline().split()))

# n개 중 3개를 뽑는 모든 경우의 수
# 그 합이 m과 가장 가까운 수
sum = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            cur_sum = card_list[i] + card_list[j] + card_list[k]
            if m - cur_sum >= 0 and sum < cur_sum:
                sum = cur_sum
                if m == cur_sum:
                    break
print(sum)

# gemini

import sys


def solve():
    # 1. Read Inputs
    n, m = map(int, sys.stdin.readline().split())
    card_list = list(map(int, sys.stdin.readline().split()))

    max_sum = 0

    # 2. Triple Loop
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                cur_sum = card_list[i] + card_list[j] + card_list[k]

                # Check constraints
                if cur_sum <= m:
                    # Update max_sum if this is better
                    if cur_sum > max_sum:
                        max_sum = cur_sum

                    # Optimization: If we hit the target exactly, stop everything!
                    if max_sum == m:
                        return max_sum

    return max_sum


# Run the function
print(solve())

# gemini 2

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

max_sum = 0

# combinations(cards, 3) automatically gives you every group of 3 cards
for combo in combinations(cards, 3):
    cur_sum = sum(combo)  # built-in sum() function is useful here!

    if cur_sum <= m and cur_sum > max_sum:
        max_sum = cur_sum

print(max_sum)
