import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = []

for i in range(n):
    n_list.append(0)

for x in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    # i = 2, j = 5
    for y in range(len(n_list)):
        if i <= y + 1:
            if j >= y + 1:
                n_list[y] = k

for i in range(len(n_list)):
    print(n_list[i], end=" ")


# gemini가 제안해준 더 개선된 코드
# import sys

# # 바구니 개수(n), 공 넣을 횟수(m) 입력
# n, m = map(int, sys.stdin.readline().split())

# # n개의 0으로 채워진 리스트 생성 (개선점 1)
# baskets = [0] * n

# for _ in range(m):
#     # 공을 넣을 바구니의 시작(i), 끝(j), 공 번호(k) 입력
#     i, j, k = map(int, sys.stdin.readline().split())

#     # i-1부터 j-1까지의 인덱스에 공 번호 k를 할당 (개선점 2)
#     for index in range(i - 1, j):
#         baskets[index] = k

# # 결과 출력 (개선점 3)
# print(*baskets)
