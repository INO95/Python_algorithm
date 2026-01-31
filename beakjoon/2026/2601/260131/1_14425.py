import sys

n, m = map(int, sys.stdin.readline().split())
s = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())
checks = [list(map(str, sys.stdin.readline().split())) for _ in range(m)]

result = 0

for check in checks:
    if check[0] in s:
        result += 1

print(result)

# gemini's feedback 1

import sys

# 1. Read N and M
n, m = map(int, sys.stdin.readline().split())

# 2. Use a SET for 'S'
#    Lookup time becomes O(1)
s = set()
for _ in range(n):
    s.add(sys.stdin.readline().rstrip())

result = 0

# 3. Process checks
for _ in range(m):
    check_word = sys.stdin.readline().rstrip()

    # 4. Check existence (Instant because 's' is a set)
    if check_word in s:
        result += 1

print(result)

# gemini's feedback 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# Create two sets
set_s = {input().rstrip() for _ in range(n)}
check_list = [input().rstrip() for _ in range(m)]

# Count how many items in check_list exist in set_s
# (We iterate the list because duplicate words in checks should be counted individually)
count = sum(1 for word in check_list if word in set_s)

print(count)

# **Summary:** Whenever you need to check "Does this item exist in that group?", always use a **Set** (`{}`) instead of a List (`[]`).
