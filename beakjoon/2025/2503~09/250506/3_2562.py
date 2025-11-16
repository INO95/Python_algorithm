import sys

list = []

for i in range(9):
    list.append(int(sys.stdin.readline().rstrip()))

n = list[0]
m = 1

for i in range(9):
    if n < list[i]:
        n = list[i]
        m = i + 1

print(n)
print(m)
