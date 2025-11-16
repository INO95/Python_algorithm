# import sys, re

# wordCnt = int(sys.stdin.readline())
# words = []


# def has_separated_duplicates(s):
#     if len(set(s)) <= 1:
#         return False
#     match = re.search(r"(.).+?\1", s)
#     return match is not None


# for i in range(wordCnt):
#     words.append(sys.stdin.readline().rstrip())
#     result = words[i][0]
#     for j in range(1, len(words[i])):
#         if words[i][j] != result[-1]:
#             result += words[i][j]
#     if not {has_separated_duplicates(result)}:
#         wordCnt -= 1

# print(wordCnt)

# 모르겠어서 제미나이한테 물어봄

# 제미니의 답
import sys

# 단어의 개수 N을 입력받음
n = int(sys.stdin.readline())
group_word_count = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    appeared_chars = []  # 이미 나타난 문자 그룹을 기록하는 리스트
    is_group_word = True  # 일단 그룹 단어라고 가정하고 시작

    for i in range(len(word)):
        # 현재 문자가 이전에 나타난 문자 그룹에 있는지 확인
        if word[i] in appeared_chars:
            # 그런데 바로 앞 문자와 같지 않다면, 그룹 단어가 아님
            if word[i] != word[i - 1]:
                is_group_word = False
                break  # 더 이상 검사할 필요 없으므로 반복 중단
        else:
            # 처음 보는 문자이면 기록에 추가
            appeared_chars.append(word[i])

    # 반복문이 중단되지 않고 끝까지 실행되었다면 그룹 단어임
    if is_group_word:
        group_word_count += 1

print(group_word_count)
