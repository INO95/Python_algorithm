import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

min = 0
sum = 0

for i in range(n, m + 1, 1):
    if i < 2:
        continue
    isPrime = True
    for j in range(2, int(i**0.5) + 1, 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        sum = sum + i
        if min == 0:
            min = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)


# i got the right answer and this is gemini's feedback

import sys


# 1. Isolate the logic into a "Helper Function"
# This makes the code reusable and readable.
def check_prime(num):
    if num < 2:
        return False
    # Standard square root optimization
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# --- Main Logic ---

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

min_prime = -1  # Use -1 to represent "Not found yet"
total_sum = 0  # Changed name from 'sum' to 'total_sum'

for i in range(n, m + 1):  # Removed ', 1' because it is default

    # The main loop becomes very clean!
    if check_prime(i):
        total_sum += i

        # If min_prime is still -1, this is the first prime we found
        if min_prime == -1:
            min_prime = i

# --- Output ---
if min_prime == -1:
    print(-1)
else:
    print(total_sum)
    print(min_prime)
