nums = [3, 2, 6, 1, 4, 0]


def missingNumber(nums) -> int:
    nums.sort()

    if nums[-1] != len(nums):
        return len(nums)
    if nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        expected = nums[i - 1] + 1
        if expected != nums[i]:
            return expected


print(missingNumber(nums))
