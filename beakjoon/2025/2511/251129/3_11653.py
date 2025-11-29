import sys

n = int(sys.stdin.readline())
i = 2
anwsers = []
while True:
    if n == 1:
        break
    if n == 2:
        anwsers.append(2)
        break
    if n % i == 0:
        anwsers.append(i)
        n = int(n / i)
        i = 2
    else:
        i += 1
    if i == n:
        anwsers.append(i)
        break
for i in range(len(anwsers)):
    print(anwsers[i])

# i got the right answer

# this is gemini's feedback no 1

import sys

n = int(sys.stdin.readline())
i = 2

# We loop until n becomes 1
while n > 1:
    # While n is divisible by i, keep dividing!
    # e.g., for 12: 12->6->3 (divides by 2 twice immediately)
    while n % i == 0:
        print(i)  # Print immediately (no need for a list)
        n //= i  # Use // for integer division

    # If n is no longer divisible by i, move to the next number
    i += 1

# and this is gemini's feedback no 2

import sys

n = int(sys.stdin.readline())
i = 2

# Optimization: Only go up to the square root of n
while i * i <= n:
    while n % i == 0:
        print(i)
        n //= i
    i += 1

# If n is still > 1 after the loop, the remaining n is a prime number
if n > 1:
    print(n)
