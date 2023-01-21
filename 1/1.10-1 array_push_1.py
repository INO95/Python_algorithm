arr = [3, 4, 2, 6, 5]

k = 2


def arrayPush(arr, k) -> None:
    for _ in range(k):
        prev = arr[len(arr) - 1]
        for i in range(len(arr)):
            temp = arr[i]
            arr[i] = prev
            prev = temp


arrayPush(arr, k)
print(arr)
