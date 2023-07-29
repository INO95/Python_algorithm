# 파스칼의 삼각형

# 처음 두 줄을 제외하고 새로 만들어지는 줄의 새로운 숫자는 윗줄의 왼쪽 수와
# 오른쪽 수를 더해 만들어진다.

numRows = 5


def triangle(numRows):
    pascal = []
    # 0일 경우 대비
    if numRows <= 0:
        return pascal
    pascal.append([1])
    for i in range(1, numRows):
        prev_len = len(pascal[i - 1])
        curr_list = []
        for j in range(prev_len + 1):
            # 처음과 끝은 1
            num = 1
            # 처음과 끝이 아닐 경우 전 행의 값 2개를 더한 값
            if j != 0 and j != prev_len:
                num = pascal[i - 1][j - 1] + pascal[i - 1][j]
            # 1 혹은 중간값을 더함
            curr_list.append(num)
        # 완성된 row를 전체에 삽입
        pascal.append(curr_list)
    print(pascal)


triangle(numRows)
