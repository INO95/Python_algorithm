import sys

matrixA = []
matrixB = []
matrixFinal = []

n, m = map(int, sys.stdin.readline().rstrip().split())

for i in range(n):
    matrix = []
    matrix = list(sys.stdin.readline().rstrip().split())
    matrixA.append(matrix)
for i in range(n):
    matrix = []
    matrix = list(sys.stdin.readline().rstrip().split())
    matrixB.append(matrix)

for i in range(n):
    matrix = []
    for j in range(m):
        total = int(matrixA[i][j]) + int(matrixB[i][j])
        matrix.append(total)
    matrixFinal.append(matrix)

for i in range(n):
    for j in range(m):
        print(matrixFinal[i][j], end=" ")
    print()

# 제미나이 제안

import sys

n, m = map(int, sys.stdin.readline().split())

# 1. 행렬 A와 B를 효율적으로 입력받음
matrixA = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
matrixB = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2. 계산과 동시에 바로 출력
for i in range(n):
    result_row = []
    for j in range(m):
        # 각 행의 결과값을 계산하여 result_row에 추가
        result_row.append(matrixA[i][j] + matrixB[i][j])

    # 3. 한 행의 계산이 끝나면 '*'를 이용해 한번에 출력 (더 간결한 방법)
    print(*result_row)
