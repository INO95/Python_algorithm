nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    for _ in range(k):
        prev = nums[len(nums) - 1]
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = prev
            prev = temp


rotate(nums, k)

print(nums)
