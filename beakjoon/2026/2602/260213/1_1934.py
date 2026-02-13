# import sys

# t = int(sys.stdin.readline())
# answers = []
# for _ in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     answer = 1
#     a_set = set()
#     b_set = set()
#     for i in range(1, a + 1):
#         if a % i == 0:
#             a_set.add(i)
#     for i in range(1, b + 1):
#         if b % i == 0:
#             b_set.add(i)

#     if len(a_set) == 1 or len(b_set) == 1:
#         answers.append(a * b)
#     elif len(a_set) == 2 or len(b_set) == 2:
#         answers.append(a * b)
#     else:
#         final_set = a_set.union(b_set)
#         final_set.remove(1)
#         final_set.remove(a)
#         final_set.remove(b)
#         for x in final_set:
#             answer = answer * x
#         answers.append(answer)

# for x in answers:
#     print(x)

# 출력 초과로 실패, gpt 어드바이스

import sys
input = sys.stdin.readline

# 최대공약수를 구함 (두 수를 모두 나눌 수 있는 수)
def gcd(a, b):
    # b가 0이 될 때 까지
    while b:
        # a에 b를 담고 b에 a에서 b를 나눈 나머지를 담음
        a, b = b, a % b
        # 유클리드 호재법이라고 함
    return a

t = int(input())
out = []
for _ in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    out.append(str(a // g * b))

print("\n".join(out))
