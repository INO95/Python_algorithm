import sys

words = []
word = ""
maxLength = 0

for _ in range(5):
    thisWord = sys.stdin.readline().rstrip()
    words.append(thisWord)
    if len(thisWord) > maxLength:
        maxLength = len(thisWord)

for i in range(maxLength):
    for j in range(5):
        if i < len(words[j]):
            word += words[j][i]

print(word)

# 제미나이 제안 1

import sys

words = [sys.stdin.readline().rstrip() for _ in range(5)]
# 가장 긴 단어의 길이를 구하는 것은 동일
max_length = max(len(w) for w in words)

result = []
for i in range(max_length):
    for j in range(5):
        try:
            # words[j]의 i번째 문자에 접근 시도
            result.append(words[j][i])
        except IndexError:
            # 문자가 없어서 에러가 나면 그냥 넘어감
            pass

print("".join(result))


# 제미나이 제안 2

from itertools import zip_longest
import sys

# 1. 5줄의 입력을 리스트로 받음
words = [sys.stdin.readline().rstrip() for _ in range(5)]

# 2. zip_longest로 세로로 묶고, 결과 리스트에 담기
result = []
# *words: ['ABC', 'DE'] -> 'ABC', 'DE' (리스트를 풀어헤쳐 인자로 전달)
for chars_in_col in zip_longest(*words, fillvalue=""):
    # chars_in_col은 ('A', 'D'), ('B', 'E'), ('C', '') 와 같은 튜플
    result.append("".join(chars_in_col))

# 3. 최종 결과 출력
print("".join(result))
