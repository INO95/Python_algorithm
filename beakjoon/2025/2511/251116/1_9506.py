import sys

divisors = []
n = 0
sum = 0

while n != -1:
    n = int(sys.stdin.readline())
    if n != -1:
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
                sum = sum + i
        if sum == n:
            print(f"{n} = ", end="")
            print(*divisors, sep=" + ")
        else:
            print(f"{n} is NOT perfect.")
        divisors.clear()
        sum = 0

# gemini's feedback

import sys

while True:
    n = int(sys.stdin.readline())

    # 1. Exit condition first
    if n == -1:
        break

    # 2. Initialize variables inside the loop
    divisors = []
    divisor_sum = 0

    # 3. Use the loop optimization
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors.append(i)
            divisor_sum += i

    # 4. Check the sum and print
    if divisor_sum == n:
        print(f"{n} = ", end="")
        print(*divisors, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")

    # 5. No cleanup code is needed!
