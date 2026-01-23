# import sys

# n = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline()) for _ in range(n)]
# nums.sort()
# sys.stdout.write("\n".join(map(str, nums)) + "\n")

# gemini's help

import sys

# 1. N을 입력받습니다.
n = int(sys.stdin.readline())

# 2. 숫자를 저장할 리스트 대신, 개수를 저장할 리스트를 만듭니다.
#    문제에서 숫자는 최대 10,000이라고 했습니다.
#    인덱스 0~10000을 사용하기 위해 크기는 10001로 만듭니다.
count_list = [0] * 10001

# 3. 입력받는 즉시 개수를 셉니다. (절대로 리스트에 append 하지 않습니다!)
for _ in range(n):
    num = int(sys.stdin.readline())
    count_list[num] += 1

# 4. 0부터 10000까지 순서대로 돕니다.
for i in range(10001):
    # 해당 숫자(i)가 1번 이상 나왔다면
    if count_list[i] != 0:
        # 그 개수만큼 반복해서 출력합니다.
        for _ in range(count_list[i]):
            print(i)
