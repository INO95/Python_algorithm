# import sys

# n, b = sys.stdin.readline().rstrip().split()
# sum = 0

# # 변환한 숫자가 기준 B진법보다 클 경우 수정
# def __base(number):
#     if number < int(b):
#         return number
#     else

# # 10 이상의 숫자인 알파벳을 10진법으로 변환
# def __numbers(alphabet):
#     match alphabet:
#         case "A":
#             return 10
#         case "B":
#             return 11
#         case "C":
#             return 12
#         case "D":
#             return 13
#         case "E":
#             return 14
#         case "F":
#             return 15
#         case "G":
#             return 16
#         case "H":
#             return 17
#         case "I":
#             return 18
#         case "J":
#             return 19
#         case "K":
#             return 20
#         case "L":
#             return 21
#         case "N":
#             return 22
#         case "M":
#             return 23
#         case "O":
#             return 24
#         case "P":
#             return 25
#         case "Q":
#             return 26
#         case "R":
#             return 27
#         case "S":
#             return 28
#         case "T":
#             return 29
#         case "U":
#             return 30
#         case "V":
#             return 31
#         case "W":
#             return 32
#         case "X":
#             return 33
#         case "Y":
#             return 34
#         case "Z":
#             return 35


# for i in range(len(n)):
#     littleSum = __numbers(n[i])
#     if i == 0:
#         sum += littleSum - 1
#     else:
#         for j in range(i):
#             littleSum += littleSum * littleSum
#         sum += littleSum
# print(sum)

# 풀다 포기하고 제미나이한테 헬프함

import sys

n, b = sys.stdin.readline().rstrip().split()
b = int(b)  # B는 숫자로 변환해야 합니다.
total_sum = 0
length = len(n)


# 1. 알파벳과 숫자를 모두 10진법 숫자로 변환하는 함수
def char_to_int(char):
    if "A" <= char <= "Z":
        # ord('A')는 65입니다. 'A'를 10으로 만들려면 55를 빼줍니다.
        return ord(char) - ord("A") + 10
    else:  # '0' ~ '9'
        # ord('0')은 48입니다. '0'을 0으로 만들려면 48을 빼줍니다.
        return ord(char) - ord("0")


# 2. 메인 루프 (왼쪽 문자부터 순회)
# i는 0, 1, 2, ... 순서로 증가
for i in range(length):
    char = n[i]
    digit = char_to_int(char)  # 문자를 10진수(0~35)로 변환

    # "자릿값" 계산이 핵심입니다!
    # i=0 (첫 글자)일 때, power는 length-1
    # i=1 (두 번째 글자)일 때, power는 length-2
    # ...
    # i=length-1 (마지막 글자)일 때, power는 0
    power = (length - 1) - i

    # 3. (숫자) x (B의 거듭제곱)을 총합에 더하기
    total_sum += digit * (b**power)

print(total_sum)


import sys

n, b = sys.stdin.readline().rstrip().split()

# 문자열 n을 b진법으로 해석해서 10진법 정수로 바꿔줘
result = int(n, int(b))

print(result)
