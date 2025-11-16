import sys

n = int(sys.stdin.readline().rstrip())
numbers = sys.stdin.readline().rstrip()
sum = 0

for index in range(n):
    sum = sum + int(numbers[index])

print(sum)


# gemini 제안

# 1

# import sys

# n = int(sys.stdin.readline())
# numbers = sys.stdin.readline().rstrip()
# total = 0 # 'sum'은 내장 함수 이름이므로 다른 변수명(total)을 쓰는 것이 좋습니다.

# for num_char in numbers:
#     total += int(num_char)

# print(total)


# 2

# import sys

# # n은 이 풀이에서는 사실상 필요 없습니다.
# sys.stdin.readline()

# # 입력받은 문자열의 각 문자에 int 함수를 적용한 후, 모두 더합니다.
# print(sum(map(int, sys.stdin.readline().rstrip())))
