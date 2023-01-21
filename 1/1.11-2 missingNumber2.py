nums = [3, 2, 6, 1, 4, 0]


def missingNumber(nums) -> int:
    set_nums = set(nums)

    for i in range(len(nums) + 1):
        if i not in set_nums:
            return i
    return -1


print(missingNumber(nums))
