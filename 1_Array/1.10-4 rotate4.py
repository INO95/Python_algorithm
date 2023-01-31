nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    k = k % len(nums)
    nums[:] = nums[::-1]
    nums[0:k] = nums[0:k][::-1]
    nums[k:len(nums)] = nums[k:len(nums)][::-1]


rotate(nums, k)

print(nums)
