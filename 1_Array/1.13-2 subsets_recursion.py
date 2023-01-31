nums = [1, 2, 3]
res = []
sub = []
index = 0


def subsets_recursion(nums, res, sub, index) -> None:
    if len(sub) > len(nums):
        return res

    res.append(sub.copy())

    for i in range(index, len(nums)):
        sub.append(nums[i])
        subsets_recursion(nums, res, sub, i + 1)
        sub.pop()


subsets_recursion(nums, res, sub, index)

print(res)
