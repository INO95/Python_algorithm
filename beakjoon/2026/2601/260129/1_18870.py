# import sys

# n = int(sys.stdin.readline())

# numbers = list(map(int, sys.stdin.readline().split()))

# sortedNumbers = sorted(set(numbers))

# for i in range(n):
#     print(sortedNumbers.index(numbers[i]), end=" ")

# timeover

# gemini's help

import sys

# 1. Input
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# 2. Sort and remove duplicates (O(N log N))
#    Ex: [2, 4, -10, 4, -9] -> [-10, -9, 2, 4]
sorted_numbers = sorted(set(numbers))

# 3. Create a Dictionary for O(1) lookup
#    Ex: {-10: 0, -9: 1, 2: 2, 4: 3}
#    This part is the KEY optimization.
rank_dict = {num: i for i, num in enumerate(sorted_numbers)}

# 4. Print results using the dictionary
#    Lookup time is now O(1) instead of O(N)
for num in numbers:
    print(rank_dict[num], end=" ")
