import sys

n, m = map(int, sys.stdin.readline().split())

people = {}
result = []
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    people[name] = True

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name in people:
        result.append(name)

result.sort()
print(len(result))
for x in result:
    print(x)


# GPT 1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

heard = {input().strip() for _ in range(n)}
res = [input().strip() for _ in range(m) if input().strip() in heard]

res.sort()
print(len(res))
print("\n".join(res))


# GPT 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

heard = set()
for _ in range(n):
    heard.add(input().strip())

res = []
for _ in range(m):
    name = input().strip()
    if name in heard:
        res.append(name)

res.sort()
sys.stdout.write(str(len(res)) + "\n")
sys.stdout.write("\n".join(res))


# tip 

heard = {input().strip() for _ in range(n)}
seen = {input().strip() for _ in range(m)}
res = sorted(heard & seen)
