import sys

S = sys.stdin.readline().rstrip()

alphabats = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

for i in range(len(alphabats)):
    for j in range(len(S)):
        isExist = False
        if S[j] == alphabats[i]:
            print(j, end=" ")
            isExist = True
            break
    if isExist == False:
        print(-1, end=" ")


# gemini 제안

# 1

# S = input() # 이 문제에서는 readline 보다 input()이 더 간편할 수 있습니다.
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in alphabet:
#     print(S.find(char), end=" ")

# 2

# S = input()
# # a부터 z까지의 위치를 저장할 리스트를 -1로 초기화합니다.
# result = [-1] * 26

# # 문자열 S를 처음부터 순회합니다.
# for i in range(len(S)):
#     char = S[i]
#     # 알파벳 순서에 맞는 인덱스를 계산합니다. (a=0, b=1, ...)
#     index = ord(char) - ord('a')

#     # 아직 위치가 기록되지 않았다면 (값이 -1이라면) 현재 위치 i를 기록합니다.
#     if result[index] == -1:
#         result[index] = i

# # *를 사용하면 리스트의 모든 요소를 공백으로 구분해 출력할 수 있습니다.
# print(*result)
