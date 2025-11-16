import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n - 1, -1, -1):
    star = ""

    for j in range(i):
        star += " "

    if len(star) < n:
        for k in range(n - len(star)):
            star += "*"

    print(star)
