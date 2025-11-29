import sys

x, y, w, h = map(int, sys.stdin.readline().split())

min_distance = x

if x > w - x:
    min_distance = w - x
if min_distance > y:
    min_distance = y
if min_distance > h - y:
    min_distance = h - y

print(min_distance)
