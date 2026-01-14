import sys

n = int(sys.stdin.readline())
cnt = 0
num_str = ""
i = 666
while True:
    i_str = str(i)
    if i_str.find("666") != -1:
        cnt += 1
        num_str = i_str
    if cnt == n:
        break
    i += 1
print(num_str)

# gemini feedback

import sys

n = int(sys.stdin.readline())

cnt = 0
num = 666

while True:
    # Check if "666" is inside the string representation
    if "666" in str(num):
        cnt += 1

    # If we found the N-th number, stop
    if cnt == n:
        print(num)
        break

    num += 1
