# prototype 1

# import sys

# n = int(sys.stdin.readline())
# i = 0
# divisors = []
# answers = []

# for _ in range(n):
#     num = int(sys.stdin.readline())
#     i = num
#     for i in range(i, 0, -1):
#         if num % i == 0:
#             divisors.append(num / i)
#     if len(divisors) == 1:
#         answers.append(num)

# print(len(answers))

# prototype 2

# import sys

# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# j = 0
# cnt = 0
# answers = []
# for i in range(n):
#     j = numbers[i]
#     for j in range(numbers[i], 0, -1):
#         if numbers[i] % j == 0:
#             cnt += 1
#         if cnt > 2:
#             j = 0
#             cnt = 0
#             break
#     if cnt == 2:
#         answers.append(numbers[i])
#         j = 0
#         cnt = 0
#     j = 0
#     cnt = 0
# print(len(answers))


# gemini's refactoring no 1

# import sys

# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# prime_count = 0

# for num in numbers:
#     # 1. Edge Case: 1 is not a prime number
#     if num < 2:
#         continue  # Skip to the next number

#     # 2. Assume it is prime until proven otherwise
#     is_prime = True

#     # 3. Check from 2 up to num - 1
#     #    (If num is 7, we check 2, 3, 4, 5, 6)
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False  # Found a divisor! Not prime.
#             break  # Stop checking immediately

#     # 4. If the flag is still True, count it
#     if is_prime:
#         prime_count += 1

# print(prime_count)

# gemini's refactoring no 2 (master)

import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
prime_count = 0

for num in numbers:
    # 1. Edge Case: 1 is not a prime number
    if num < 2:
        continue  # Skip to the next number

    # 2. Assume it is prime until proven otherwise
    is_prime = True
    # checking up to int(num ** 0.5) + 1 saves huge amount of time for big numbers
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # 4. If the flag is still True, count it
    if is_prime:
        prime_count += 1

print(prime_count)
