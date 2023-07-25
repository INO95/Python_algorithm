# 파스칼의 삼각형 만들기

# 크기 선언
numRows = 6


def generate(numRows) -> list:
    # 초기 배열 선언
    pascal = []

    # 만약 크기가 0 이하라면 return
    if numRows <= 0:
        return pascal

    # 초기 데이터인 1을 넣어준다.
    pascal.append([1])

    # 1부터 시작하는 이유는 초기값이 이미 있기 때문에
    for i in range(1, numRows):
        # 이전 수행식에서의 길이를 저장한다.
        prev_len = len(pascal[i - 1])
        # 삽입할 배열의 초기값 선언
        curr_list = []

        # 길이를 하나 더 늘려야 하기 때문에 (i + 1) 이 된다.
        for j in range(i + 1):
            num = 1
            # 추가할 배열의 첫 번째 요소와 마지막 요소가 아닌 경우
            if j != 0 and j != prev_len:
                # 위치 기준으로 두 개의 요소를 선정하여 더한다.
                num = pascal[i - 1][j - 1] + pascal[i - 1][j]

            curr_list.append(num)

        pascal.append(curr_list)

    return pascal


print(generate(numRows))
