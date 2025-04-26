nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    # 이동할 거리를 미리 계산
    k = k % len(nums)
    # 배열을 뒤집는다.
    nums[:] = nums[::-1]
    # k를 기준으로 배열의 앞부분을 뒤집는다.
    nums[0:k] = nums[0:k][::-1]
    # k를 기준으로 배열의 뒷부분을 뒤집는다.
    nums[k:len(nums)] = nums[k:len(nums)][::-1]


rotate(nums, k)

print(nums)
