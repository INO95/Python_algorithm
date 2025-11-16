X = int(input())
N = int(input())
addNum = 0

for i in range(N):
    a, b = map(int, input().split())
    addNum += a * b

if addNum == X:
    print("Yes")
else:
    print("No")
