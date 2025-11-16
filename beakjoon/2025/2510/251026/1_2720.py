import sys

num = int(sys.stdin.readline())
tc = []
q = 25
d = 10
n = 5
p = 1

for _ in range(num):
    c = int(sys.stdin.readline())
    result = ""
    if c // q > 0:
        result = str(c // q)
        c = c % q
    else:
        result = result + "0"
    if c // d > 0:
        result = result + str(c // d)
        c = c % d
    else:
        result = result + "0"
    if c // n > 0:
        result = result + str(c // n)
        c = c % n
    else:
        result = result + "0"
    if c // p > 0:
        result = result + str(c // p)
    else:
        result = result + "0"
    tc.append(result)
for i in range(len(tc)):
    for j in range(len(tc[i])):
        if j == len(tc[i]) - 1:
            print(tc[i][j], end="")
        else:
            print(tc[i][j], end=" ")
    print()

# 자꾸 틀렸다고 함
# 제미나이가 이게 맞다고 함
import sys

num = int(sys.stdin.readline())

# 코인 값을 리스트로 관리하면 더 좋습니다.
coins = [25, 10, 5, 1]

for _ in range(num):
    c = int(sys.stdin.readline())

    # 결과를 저장할 리스트
    result_counts = []

    for coin in coins:
        # 1. 해당 코인으로 나눈 몫(개수)을 구합니다.
        count = c // coin
        result_counts.append(count)

        # 2. 남은 돈(c)을 나머지로 갱신합니다.
        c = c % coin

    # 3. 한 줄의 계산이 끝나면, 리스트의 모든 요소를 공백으로 구분해 출력합니다.
    print(*result_counts)


# 제미나이 제안
import sys

num = int(sys.stdin.readline())

# 25, 10, 5, 1 순서대로 계산
q = 25
d = 10
n = 5
p = 1

for _ in range(num):
    c = int(sys.stdin.readline())

    # 1. 쿼터(q) 계산
    q_count = c // q
    c = c % q  # 쿼터를 주고 남은 돈으로 c를 갱신

    # 2. 다임(d) 계산
    d_count = c // d
    c = c % d  # 다임을 주고 남은 돈으로 c를 갱신

    # 3. 니켈(n) 계산
    n_count = c // n
    c = c % n  # 니켈을 주고 남은 돈으로 c를 갱신

    # 4. 페니(p) 계산 (마지막엔 나머지를 계산할 필요 없음)
    p_count = c // p

    # 5. 결과를 바로 출력 (리스트에 저장할 필요 없음)
    print(q_count, d_count, n_count, p_count)
