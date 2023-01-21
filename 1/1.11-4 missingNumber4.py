nums = [3, 2, 6, 1, 4, 0]


def missingNumber(nums) -> int:
    expected_sum = 0
    nums_sum = 0

    for i in range(len(nums) + 1):
        expected_sum += i

    for _, num in enumerate(nums):
        nums_sum += num

    return expected_sum - nums_sum


print(missingNumber(nums))


def missingNumber2(nums) -> int:
    expected_sum = int((len(nums) * (len(nums) + 1)) / 2)
    nums_sum = 0
    for _, num in enumerate(nums):
        nums_sum += num
    return expected_sum - nums_sum


print(missingNumber2(nums))


def missingNumber3(nums) -> int:
    return int((len(nums) * (len(nums) + 1)) / 2) - sum(nums)


print(missingNumber3(nums))
