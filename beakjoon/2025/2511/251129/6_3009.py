import sys

# x, y 값에서 같은 값이 각 2개씩 나와야하고,
# 1개만 나온 값을 출력하면 됩
x_values = []
y_values = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_values.append(x)
    y_values.append(y)

x_value = 0
y_value = 0
for i in range(3):
    if x_values.count(x_values[i]) == 1:
        x_value = x_values[i]
        break

for i in range(3):
    if y_values.count(y_values[i]) == 1:
        y_value = y_values[i]
        break
print(x_value, end=" ")
print(y_value)

# gemini's feedback no.1
import sys
from collections import Counter

x_values = []
y_values = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_values.append(x)
    y_values.append(y)

# Counter creates a dictionary like: {30: 2, 10: 1}
x_counts = Counter(x_values)
y_counts = Counter(y_values)

# Find the item where the count is 1
# .items() gives us (key, value) pairs
for key, value in x_counts.items():
    if value == 1:
        print(key, end=" ")

for key, value in y_counts.items():
    if value == 1:
        print(key)

# gemini's feedback no.2
import sys

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

# Calculate X
if x_list[0] == x_list[1]:
    x = x_list[2]
elif x_list[0] == x_list[2]:
    x = x_list[1]
else:
    x = x_list[0]

# Calculate Y
if y_list[0] == y_list[1]:
    y = y_list[2]
elif y_list[0] == y_list[2]:
    y = y_list[1]
else:
    y = y_list[0]

print(x, y)

# gemini's feedback no.3
x = 0
y = 0
# ... input collecting code ...

# "Look at the list, find the 'num' where its count is 1, and give me the first result"
x = [num for num in x_values if x_values.count(num) == 1][0]
y = [num for num in y_values if y_values.count(num) == 1][0]

print(x, y)
# gemini's feedback no.4

import sys

x_ans = 0
y_ans = 0

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())

    # The pairs will cancel out to 0, leaving only the unique number
    x_ans = x_ans ^ x  # XOR operation
    y_ans = y_ans ^ y  # XOR operation

print(x_ans, y_ans)
