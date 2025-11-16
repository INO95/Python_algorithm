import sys

word = list(sys.stdin.readline().rstrip())
cntDict = dict()

for i in range(len(word)):
    cntDict[word[i].lower()] = 0

for i in range(len(word)):
    cntDict[word[i].lower()] += 1

cnt = 0
winner = ""
for key, value in cntDict.items():
    if value == cnt:
        winner = "?"
    if value > cnt:
        cnt = value
        winner = key

print(winner.upper())


# 제미나이 제안

import sys

# 1. 단어를 읽고 바로 대문자로 변경합니다.
word = sys.stdin.readline().strip().upper()

# 2. 단어에 사용된 알파벳 중 중복을 제거한 목록을 만듭니다.
unique_letters = list(set(word))

# 3. 각 알파벳의 개수를 셉니다.
counts = []
for letter in unique_letters:
    counts.append(word.count(letter))

# 4. 가장 많이 나온 횟수를 찾고, 그 횟수가 리스트에 여러 번 있는지 확인합니다.
max_count = max(counts)
if counts.count(max_count) > 1:
    print("?")
else:
    # 가장 많이 나온 횟수의 인덱스를 찾아, 해당 인덱스의 알파벳을 출력합니다.
    winner_index = counts.index(max_count)
    print(unique_letters[winner_index])
