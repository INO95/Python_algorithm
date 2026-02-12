import sys

str_S = sys.stdin.readline().rstrip()

str_can_be = set()

for i in range(len(str_S)):
    for j in range(1, len(str_S) + 1):
        target = str_S[i : j]
        if target != '':
            str_can_be.add(target)

print(len(str_can_be))

# GPT's feedback

import sys

S = sys.stdin.readline().strip()
sub = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        sub.add(S[i:j])

print(len(sub))


