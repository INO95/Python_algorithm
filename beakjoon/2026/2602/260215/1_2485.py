# # 각 가로수마다 떨어져 있는 거리를 구한다?
# # 1, 3, 7, 13 이면 가장 짧은 거리가 1이랑 3이니까 여기에 맞춰야 함
# # 각 거리는 2, 4, 6이니까 4랑 6에서 2가 되도록 하려면 2 * 3이라서 3
# # 2, 6, 12, 18이면 4
# # 4, 6, 6인데 이러면 여기의 최대공약수인 2를 기준으로 해야 함
# # 그러면 1, 2, 2라서 5
# # 즉, 모든 수의 최대공약수를 구해서 각 거리와 최대공약수의 차가 될 만큼 빼준 값
# # 1. 거리를 구하면서 모든 값의 거리의 차를 저장한다
# # 2. 구한 값들의 최대공약수를 구한다
# # 3. 구한 값들이 최대공약수가 되려면 필요한 값에서 최대공약수를 나눈 값을 모두 더해서 출력한다.

# import sys

# input = sys.stdin.readline

# n = int(input())
# prev_distance = 0
# distances = []
# dis_gcd = 0
# answer = 0

# def getGcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# for i in range(n):
#     distance = int(input())
#     diff = 0

#     if 0 < i:
#         diff = distance - prev_distance
#         prev_distance = distance
#         distances.append(diff)
#     else:
#         prev_distance = distance
    
# # i = 0 일때는 처리 불필요
# # i 가 1 이상부터는 다음 숫자와의 최대공약수를 구함
# # 그 이후부터는 구한 최대공약수와 다음 숫자와의 최대공약수를 구함
# for i in range(len(distances)):
#     if 0 < i:
#         diff = distances[i]
#         prevDiff = distances[i-1]

#         tmp_gcd = getGcd(prevDiff, diff)

#         if tmp_gcd > dis_gcd:
#             dis_gcd = tmp_gcd
#     else:
#         dis_gcd = getGcd(distances[0], distances[1])

# for i in range(len(distances)):
#     if dis_gcd > 0:
#         answer = answer + ((distances[i] - dis_gcd) // dis_gcd)


# print(answer)


# 지피티 헬프

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
pos = [int(input()) for _ in range(n)]

# 인접한 가로수 사이 거리들의 gcd(최대공약수)를 구한다
g = pos[1] - pos[0]
for i in range(2, n):
    g = gcd(g, pos[i] - pos[i-1])

# 각 구간에 추가로 심어야 하는 개수 합산
answer = 0
for i in range(1, n):
    answer += (pos[i] - pos[i-1]) // g - 1

print(answer)
