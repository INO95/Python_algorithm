import sys

#                         1/1 →
#                   2/1 → 1/2 →
#             3/1 → 2/2 → 1/3 →
#       4/1 → 3/2 → 2/3 → 1/4 →
# 5/1 → 4/2 → 3/3 → 2/4 → 1/5 →

# x = int(sys.stdin.readline())
# numList = []
# i = 1
# while True:
#     k = i
#     for j in range(1, i + 1):
#         numList.append(str(k) + "/" + str(j))
#         k -= 1
#     i += 1
#     if len(numList) > x:
#         print(numList[x - 1])
#         break
# -> 시간초과

# x = int(sys.stdin.readline())
# numList = []
# i = 1
# for _ in range(x):

#     k = i
#     for j in range(1, i + 1):
#         numList.append(str(k) + "/" + str(j))
#         k -= 1
#     i += 1
# print(numList[x - 1])
# -> 이것도 시간초과...

# x = int(sys.stdin.readline())
# numList = []
# i = 1
# for _ in range(x):

#     k = i
#     for j in range(1, i + 1):
#         numList.append(str(k) + "/" + str(j))
#         k -= 1
#     i += 1
# print(numList[x - 1])

# 루프 횟수 1일 때  1/1 1개
# 루프 횟수 2일 때  1/1 -> 2/1 -> 1/2 3개
# 루프 횟수 3일 때  1/1 -> 2/1 -> 1/2 -> 1/3 -> 2/2 -> 1/3 5개
# 루프 횟수가 홀수면 큰 수에서 작은 수로
# 루프 횟수가 짝수면 작은 수에서 큰 수로
#  -> 분자는 1부터 점점 커짐
#  -> 분모는 loopCnt부터 점점 작아짐
# -> 배열의 길이가 2씩 늘어난다?
# x값에서 2가 들어갈 수 있는 숫자만큼의 루프 횟수
# 루프 횟수 1일 때의 x값 : 1
# 루프 횟수 2일 때의 x값 : 2~3
# 루프 횟수 3일 때의 x값 : 4~6
# 루프 횟수 4일 때의 x값 : 7~10
# 루프 횟수만큼 더해짐
# x가 10이면 x <= 4 + 3 + 2 + 1
# x가 11이면 x <= 5 + 4 + 3 + 2 + 1

# x = int(sys.stdin.readline())
# numList = []
# loopCnt = 0
# sum = 0
# while x > sum:
#     loopCnt += 1
#     sum = sum + loopCnt
# for _ in range(loopCnt, 1, -1):
#     #  짝수
#     #  -> 분자는 1부터 점점 커짐
#     #  -> 분모는 loopCnt부터 점점 작아짐
#     if loopCnt / 2 == 1:
#         i = 1
#         j = loopCnt
#         for _ in range(loopCnt):
#             numList.append(str(i) + "/" + str(j))
#             i += 1
#             j -= 1
#     #  홀수
#     #  -> 분자는 loopCnt부터 점점 작아짐
#     #  -> 분모는 1부터 점점 커짐
#     else:
#         i = loopCnt
#         j = 1
#         for _ in range(loopCnt):
#             numList.append(str(i) + "/" + str(j))
#             i -= 1
#             j += 1

# print(numList)


# x = int(sys.stdin.readline())
# numList = []
# # x가 5일 때
# # 1/1 → 1/2 → 2/1 → 3/1 → '2/2'
# i = 1
# j = 1
# maxI = 1
# maxJ = 1
# for k in range(x):
#     if numList[k][0] == 1 or numList[k][1] == 1:
#         if numList[k][0] == 1:
#             maxJ += 1
#         else:
#             maxI += 1
#     else:
#         numList.append({i, j})
#     i += 1
#     j += 1
# print(numList)
# 아 모르겟땅 도와줘 제미니

import sys

x = int(sys.stdin.readline())

# 1단계: X가 몇 번째 라인에 있는지,
#        그 라인의 몇 번째 순서인지 찾기
line = 1
while x > line:
    x -= line
    line += 1

# 2단계: line(라인 번호)과 x(라인 내 순서)로 분자/분모 계산
if line % 2 == 0:  # 짝수 라인 (분자 증가, 분모 감소)
    top = x
    bottom = line - x + 1
else:  # 홀수 라인 (분자 감소, 분모 증가)
    top = line - x + 1
    bottom = x

print(f"{top}/{bottom}")
