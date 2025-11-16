import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(word[0] + word[len(word) - 1])

# gemini 제안

# import sys

# n = int(sys.stdin.readline()) # int()는 앞뒤 공백/개행을 알아서 처리하므로 rstrip() 생략 가능

# for _ in range(n):
#     word = sys.stdin.readline().rstrip()
#     # 마지막 문자를 word[-1]로 간단하게 가져올 수 있습니다.
#     print(word[0] + word[-1])
