import sys

n = int(sys.stdin.readline())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x, y])

min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000
for i in range(n):
    if points[i][0] < min_x:
        min_x = points[i][0]
    if points[i][0] > max_x:
        max_x = points[i][0]
    if points[i][1] < min_y:
        min_y = points[i][1]
    if points[i][1] > max_y:
        max_y = points[i][1]


print((max_x - min_x) * (max_y - min_y))


# gemini's feedback 1

import sys

n = int(sys.stdin.readline())

x_coords = []
y_coords = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_coords.append(x)
    y_coords.append(y)

# Python calculates min/max for us instantly
width = max(x_coords) - min(x_coords)
height = max(y_coords) - min(y_coords)

print(width * height)

# gemini's feedback 2

import sys

n = int(sys.stdin.readline())

# Initialize with extreme values
min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # Update min/max immediately. No list needed!
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))
