import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    number = int(sys.stdin.readline())
    nums.append(number)

nums.sort()

for i in range(n):
    print(nums[i])

# gemini

import sys

# 1. Fast Input
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

# 2. Fast Sort (O(N log N))
nums.sort()

# 3. Fast Output
# Printing 1 million lines individually is slow.
# This prints everything at once, separated by new lines.
print(*nums, sep="\n")

# gemini 2
import sys

# ... sorting done ...
sys.stdout.write("\n".join(map(str, nums)) + "\n")
# This converts numbers to strings, joins them with newlines, and writes the massive string to the console instantly. For Problem 2751, the `print(*nums, sep='\n')` method is usually sufficient!
