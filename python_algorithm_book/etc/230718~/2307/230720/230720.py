# 정렬된 배열들의 요소들을 중복 없이 단 1번씩만 가질 수 있도록 주어진 배열을 그대로 수정하고, 수정된 배열의 새로운 길이를 반환하라

arr = [1, 4, 5, 5, 8, 8, 9]


def getLength(arr) -> int:
    length = 1
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            length += 1
    return length


print(getLength(arr))
