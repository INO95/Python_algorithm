import sys, math

input = sys.stdin.readline

# 일단 1이 무조건 있으니까 모든 수가 대상임

n = int(input())

print(int(math.sqrt(n)))
# int(n ** 0.5)


# window_cnt = 0

# 3이라고 하면 1, 2, 3 중에서
# 1은 1번
# 2는 2번
# 3은 2번 나와서 각각 1, 0, 0임
# 4까지 있으면 1, 2, 4에서 총 3번이라서 1
# 6까지 있으면 1, 2, 3, 6에서 총 4번이라서 0
# 즉, 그 수가 홀수가 나오면 결국 1이고 짝수가 나오면 0임
# 그 수가 짝수인지, 홀수인지 아는 방법은
# 약수의 갯수를 파악하면 된다


# for i in range(1, n + 1):
#     number_now = i
#     divisor_count = 0

#     for j in range(1, number_now + 1):
#         if number_now % j == 0:
#             divisor_count += 1
#     if divisor_count % 2 != 0:
#         window_cnt += 1
# print(window_cnt)