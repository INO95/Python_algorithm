import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

# x = (c - (b * y)) / a
# y = (f - (d * x)) / e

x = 0
y = 0

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a * i + b * j == c and d * i + e * j == f:
            x = i
            y = j
            break
print(x, y)

# if a < d:
#     num1 = d
#     num2 = e
#     num3 = f
#     d = a
#     e = b
#     f = c
#     a = num1
#     b = num2
#     c = num3

# added_x_num = a - d
# (b * y) - (e * added_x_num * y) = c - f * added_x_num
# (b - (e * added_x_num))* y = c - f * added_x_num
# y = (c - f * added_x_num) / (b - (e * added_x_num))
# x = (c - b * y) / a
# print(x, y)
