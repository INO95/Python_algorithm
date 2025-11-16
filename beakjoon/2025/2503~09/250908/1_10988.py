import sys

w = list(sys.stdin.readline().rstrip())

isP = True

for i in range(len(w)):
    if i < len(w) - i:
        if w[i] != w[len(w) - 1 - i]:
            isP = False

if isP:
    print("1")
else:
    print("0")


# 제미나이 제안 1

import sys

word = sys.stdin.readline().rstrip()

if word == word[::-1]:
    print(1)
else:
    print(0)

# 제미나이 제안 2

import sys

word = sys.stdin.readline().rstrip()

reversed_word = "".join(reversed(word))

if word == reversed_word:
    print(1)
else:
    print(0)

# 제미나이 제안 3

import sys

word = sys.stdin.readline().rstrip()
is_palindrome = 1  # 기본값을 1로 설정

# 단어 길이의 절반까지만 반복
for i in range(len(word) // 2):
    # i번째 문자와 뒤에서 i번째 문자를 비교
    if word[i] != word[-1 - i]:
        is_palindrome = 0  # 다르면 0으로 바꾸고 반복 종료
        break

print(is_palindrome)
