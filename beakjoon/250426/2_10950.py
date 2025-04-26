T = int(input())

Array = []

for i in range(T):
    A, B = map(int, input().split())

    Array.append(A + B)

for i in range(T):
    print(Array[i])
