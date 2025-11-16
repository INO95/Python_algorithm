import sys

n, k = map(int, sys.stdin.readline().split())

i = 1
yaksu = []
for _ in range(n):
    if n % i == 0:
        yaksu.append(i)
    i += 1
if len(yaksu) < k:
    print(0)
else:
    print(yaksu[k - 1])

# by gemini

import sys

n, k = map(int, sys.stdin.readline().split())

divisor_count = 0

# A more standard way to loop from 1 to n
for i in range(1, n + 1):
    # 1. Check if 'i' is a divisor
    if n % i == 0:
        # 2. If it is, increment our counter
        divisor_count += 1

    # 3. Check if this is the K-th divisor we're looking for
    if divisor_count == k:
        print(i)
        break  # Found it! Stop the loop.

else:
    # 4. This 'else' block ONLY runs if the 'for' loop
    #    finishes normally (i.e., 'break' was never called).
    #    This means we never found the K-th divisor.
    print(0)
