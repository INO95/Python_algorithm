import sys

t = int(sys.stdin.readline().rstrip())
arr = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    m = {"a": a, "b": b, "sum": a + b}
    arr.append(m)

for i in range(len(arr)):
    print(f"Case #{i + 1}: {arr[i]['a']} + {arr[i]['b']} = {arr[i]['sum']}")
