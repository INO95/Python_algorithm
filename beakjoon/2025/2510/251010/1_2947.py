import sys

word = sys.stdin.readline().strip()

c_words = [
    "c=",
    "c-",
    "dz=",
    "d-",
    "lj",
    "nj",
    "s=",
    "z=",
]

cnt = 0
for i in range(len(c_words)):
    cnt = cnt + word.count(c_words[i])
    replacedWord = word.replace(c_words[i], "@")
    word = replacedWord
replacedWord = word.replace("@", "")
word = replacedWord
print(cnt + len(word))


# 제미니 제안

import sys

word = sys.stdin.readline().strip()
croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for croatian in croatian_alphabets:
    word = word.replace(croatian, "x")  # 크로아티아 알파벳을 한 글자 'x'로 교체

print(len(word))
