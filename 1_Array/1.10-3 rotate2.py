nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    # 빈 공간의 배열을 만든다.
    temp = [0] * len(nums)

    for i, elem in enumerate(nums):
        # i + k 값에서 원 배열의 길이를 나눈 나머지
        temp[(i + k) % len(nums)] = nums[i]

    # 값에 의한 호출이 아닌 참조에 의한 호출로 사용하기 위한 slice
    nums[:] = temp


rotate(nums, k)

print(nums)
