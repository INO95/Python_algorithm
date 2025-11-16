import sys

R = int(sys.stdin.readline())

for _ in range(R):
    P = ""
    n, S = map(str, sys.stdin.readline().split())
    num = int(n)
    for index in range(len(S)):
        for _ in range(num):
            P = P + S[index]
    print(P)


# gemini 제안

# 1

# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     n, S = sys.stdin.readline().split()
#     R = int(n)

#     for char in S:
#         print(char * R, end="") # 각 문자를 R번 반복해서 바로 출력
#     print() # 테스트 케이스가 끝나면 줄바꿈

# 2

# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     n, S = sys.stdin.readline().split()
#     R = int(n)
#     result_list = []

#     for char in S:
#         result_list.append(char * R)

#     print("".join(result_list))
