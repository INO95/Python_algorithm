import sys

# 각 자릿수는 무조건 1의 자리
# 즉 9 * n의 자릿수 의 반복 안에서 찾을 수 있음
# 일단 자릿수 만큼의 리스트를 생성
# 그리고 분해합이 완성되는 조건문을 넣음
# 조건이 만족되면 완성

# n = sys.stdin.readline().rstrip()
# son_list = []
# son_index = len(n) - 1

# for _ in range(len(n)):
#     son_list.append(9)


# while True:
#     son_sum = 0
#     for i in range(len(n)):
#         son_sum = son_sum + son_list[i]
#     first_son = str(int(n) - son_sum)
#     first_son_sum = 0
#     for i in range(len(n)):
#         first_son_sum += int(first_son[i])

#     if int(first_son) + first_son_sum == int(n):
#         break

#     if son_list[son_index] != 1:
#         son_list[son_index] -= 1
#     else:
#         if son_index != 0:
#             son_index -= 1
#         else:
#             first_son = "0"
#             break

# print(first_son)

# feedback by gemini
n_str = sys.stdin.readline().rstrip()
n = int(n_str)
digit_len = len(n_str)

# 탐색 시작점: N - (9 * 자릿수)
# 단, 시작점이 음수가 되지 않도록 0과 비교해서 큰 값을 선택
start = max(1, n - (9 * digit_len))

result = 0
for i in range(start, n):
    if i + sum(map(int, str(i))) == n:
        result = i
        break

print(result)

# gemini 2

import sys

# 1. 입력 받기
n = int(sys.stdin.readline())

result = 0

# 2. 1부터 n까지 모든 숫자를 하나씩 생성자로 가정하고 검사해봅니다.
# (최적화 팁: range(max(1, n - len(str(n)) * 9), n) 으로 범위를 줄일 수도 있습니다.)
for i in range(1, n + 1):

    # 3. 분해합 계산: i + (i의 각 자릿수의 합)
    # map(int, str(i))는 숫자 i를 문자열로 바꿔서 한 글자씩 쪼갠 뒤 다시 숫자로 리스트화합니다.
    # 예: 245 -> "245" -> [2, 4, 5] -> sum([2, 4, 5]) = 11
    digits_sum = sum(map(int, str(i)))
    decomposition_sum = i + digits_sum

    # 4. 분해합이 입력값 n과 같다면, i가 가장 작은 생성자입니다.
    if decomposition_sum == n:
        result = i
        break

# 5. 결과 출력
print(result)
