import sys

n = str(sys.stdin.readline().rstrip())

strlist = []
for i in range(len(n)):
    num = n[i]
    strlist.append(num)
strlist.sort(reverse=True)

for i in range(len(n)):
    print(strlist[i], end="")

# gemini's feedback

import sys

# 1. Read input (it is already a string)
n = sys.stdin.readline().rstrip()

# 2. Sort directly using sorted()
# sorted() returns a list, so we don't need to convert n to list first.
sorted_list = sorted(n, reverse=True)

# 3. Join and print
print("".join(sorted_list))
