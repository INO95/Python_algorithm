import sys

n = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))

scores.sort()
scores.reverse()

best_score = scores[0]

for i in range(n):
    scores[i] = scores[i] / best_score * 100

sum = 0
for i in range(n):
    sum = sum + scores[i]

print(sum / n)

# gemini가 제안한 코드

# import sys

# n = int(sys.stdin.readline())
# scores = list(map(int, sys.stdin.readline().split()))

# # 1. 원래 점수 리스트에서 최댓값과 총합을 바로 구함
# max_score = max(scores)
# total_sum = sum(scores)

# # 2. 정리된 수식을 이용해 새로운 평균을 한 번에 계산
# new_average = total_sum * 100 / max_score / n

# print(new_average)
