# 재귀함수 - 모든 배열의 요소의 합 구하기

arr = [1, 2, 3, 4, 5]


def sum_elements(arr):
    if len(arr) == 1:
        return arr[0]

    return arr[0] + sum_elements(arr[1:])


print(sum_elements(arr))


nums = [1, 2]
subset = [False, False]
target = 3
i = 0


def group_sum(nums, subset, target, i) -> bool:
    if i == len(nums):
        subset_sum = 0
        for i, v in enumerate(nums):

            if subset[i]:
                subset_sum += v
        return (subset_sum == target)

    subset[i] = False
    not_select = group_sum(nums, subset, target, i + 1)
    subset[i] = True
    select = group_sum(nums, subset, target, i + 1)

    return (not_select | select)


print(group_sum(nums, subset, target, i))
