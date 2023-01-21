# using binary

nums = [1, 2, 3]


def subsets(nums) -> nums:
    res = []
    nums_len = len(nums)
    nth_bit = 1 << nums_len

    for i in range(2 ** nums_len):
        bitmask = bin(i | nth_bit)[3:]

        res.append(
            [nums[j] for j in range(nums_len) if bitmask[j] == '1']
        )
    return res


print(subsets(nums))
