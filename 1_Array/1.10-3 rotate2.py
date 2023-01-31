nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    temp = [0] * len(nums)

    for i, elem in enumerate(nums):
        temp[(i + k) % len(nums)] = nums[i]

    nums[:] = temp


rotate(nums, k)

print(nums)
