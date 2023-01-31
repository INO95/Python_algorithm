nums = [3, 2, 6, 1, 4, 0]

print(1 ^ 3)


def missingNumber(nums) -> int:
    missing = len(nums)

    for i in range(len(nums)):
        print(missing ^ i)
        print(i ^ nums[i])
        missing = missing ^ i ^ nums[i]

    return missing


print(missingNumber(nums))
