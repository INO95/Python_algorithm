# 내가 낸 정답이 틀린 이유

# 해당 코드가 틀린 이유는 입력으로 공백만 들어오거나 아무것도 입력되지 않았을 때 잘못된 결과를 출력하기 때문입니다.

# strip()은 문자열 양 끝의 공백을 모두 제거합니다. 만약 입력이 "   " (공백 3개)이라면, word는 "" (빈 문자열)이 됩니다. 코드는 이 빈 문자열에 대해 단어 개수를 1로 계산하여 출력하지만, 정답은 0입니다.

# import sys

# word = sys.stdin.readline().strip().split()
# count = 1

# for index in range(len(word)):
#     if word[index] == " ":
#         count = count + 1

# print(count)


# gemini 제안

import sys

# 입력을 받고 양 끝 공백을 제거한 뒤, 공백을 기준으로 나눔
word_list = sys.stdin.readline().strip().split()

# split()은 자동으로 단어들의 리스트를 만들어주므로, 그 길이를 출력하면 끝.
print(len(word_list))
