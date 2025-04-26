# XOR 연산을 이용
# 같으면 0, 다르면 1
# 추후 복습 요망

nums = [3, 2, 6, 1, 4, 0]


def missingNumber(nums) -> int:
    missing = len(nums)

    for i in range(len(nums)):
        missing = missing ^ i ^ nums[i]

    return missing


print(missingNumber(nums))
