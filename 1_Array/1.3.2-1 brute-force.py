nums = [2, 7, 8, 11]
target = 9


def twoSum(nums, target) -> nums:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) is target:
                return [i, j]
            return [-1, -1]


print(twoSum(nums, target))
