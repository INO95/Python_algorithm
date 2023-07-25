# 설정한 k의 수 만큼 뒤에서부터 지정하고
# 그대로 앞의 배열 요소와 자리를 바꾼다.


arr = [3, 4, 2, 6, 5]

k = 3


def arrayPush(arr, k) -> None:
    # k만큼 loop
    for _ in range(k):
        # 마지막 칸의 요소를 저장한다.
        prev = arr[len(arr) - 1]
        # 한 칸씩 당긴다.
        for i in range(len(arr)):
            # i번째 요소와 prev를 교환
            temp = arr[i]
            arr[i] = prev
            prev = temp


arrayPush(arr, k)
print(arr)
