import sys

words = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", ""]

S = sys.stdin.readline().rstrip()
time = 0

for i in range(len(S)):
    for j in range(len(words)):
        for k in range(len(words[j])):
            if S[i] == words[j][k]:
                time = time + j + 2

print(time)

# gemini 제안

# 1

# import sys

# # 각 알파벳이 몇 초 걸리는지 딕셔너리로 미리 만듭니다.
# dial = {
#     'A': 3, 'B': 3, 'C': 3,
#     'D': 4, 'E': 4, 'F': 4,
#     'G': 5, 'H': 5, 'I': 5,
#     'J': 6, 'K': 6, 'L': 6,
#     'M': 7, 'N': 7, 'O': 7,
#     'P': 8, 'Q': 8, 'R': 8, 'S': 8,
#     'T': 9, 'U': 9, 'V': 9,
#     'W': 10, 'X': 10, 'Y': 10, 'Z': 10
# }

# S = sys.stdin.readline().rstrip()
# time = 0

# # 입력받은 문자열을 순회하며 딕셔너리에서 시간 값을 찾아 더합니다.
# for char in S:
#     time += dial[char]

# print(time)

# 2

# import sys

# words = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# S = sys.stdin.readline().rstrip()
# time = 0

# for char in S:
#     for i, dial_group in enumerate(words):
#         if char in dial_group:
#             # i가 0부터 시작하므로 +3을 해줍니다 (0->"ABC"->3초)
#             time += i + 3
#             break # 찾았으면 더 이상 반복할 필요가 없으므로 탈출

# print(time)
