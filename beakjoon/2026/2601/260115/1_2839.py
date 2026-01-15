import sys

n = int(sys.stdin.readline())

cnt = 0

# while True:
#     if n == 0:
#         print(cnt)
#         break
#     elif n % 5 == 0:
#         n = n - 5
#         cnt += 1
#     elif n % 3 == 0:
#         n = n - 3
#         cnt += 1
#     elif (n - 5) % 3 == 0:
#         n = n - 5
#         cnt += 1
#     elif (n - 3) % 5 == 0:
#         n = n - 3
#         cnt += 1
#     else:
#         print(-1)
#         break

# gemini

while n >= 0:
    # 1. If divisible by 5, this is the most efficient way!
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break

    # 2. If not, we MUST take a 3kg bag to change the number
    n -= 3
    cnt += 1

# 3. If the loop finishes (n becomes negative), it's impossible
else:
    print(-1)
