import sys

num1, num2 = map(str, sys.stdin.readline().split())

num1 = num1[::-1]
num2 = num2[::-1]

if num1 > num2:
    print(num1)
else:
    print(num2)

# gemini 제안

# # 입력을 받아 split()으로 나눔
# a, b = input().split()

# # 각 문자를 뒤집은 후, max()로 둘 중 더 큰 값을 바로 출력
# print(max(a[::-1], b[::-1]))
