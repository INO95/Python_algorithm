nums = [0, 0, 1, 1, 1, 2]


def removeDuplicates(nums) -> int:
    if len(nums) <= 0:
        return 0

    curr = nums[0]
    cnt = 1

    for i in range(1, len(nums)):
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr
            cnt += 1

    return cnt


print(removeDuplicates(nums))
