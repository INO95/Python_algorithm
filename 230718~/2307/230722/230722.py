# 정렬된 배열과 목푯값이 주어지는데 목푯값을 찾는다면 배열의 해당 인덱스를 반환하고,
# 찾지 못한다면 정렬된 배열이 되도록 목표값이 배열에 들어가야 하는 인덱스를 구하라

nums = [1, 2, 3, 4, 5]
target = 3
target2 = 4


def findIndex(nums, target) -> int:
    for i in range(0, len(nums)):
        if (nums[i] == target):
            return print("index is : ", i)
        if (nums[i] + 1 == target):
            return print("index is ", i + 1)


# findIndex(nums, target)


def findIndex2(nums, target) -> int:
    index = 0

    while index < len(nums):
        if target <= nums[index]:
            break

        index += 1

    return index


print(findIndex2(nums, target))
