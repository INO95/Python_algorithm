# 선형 순회

nums = [1, 2, 3, 4, 5]

nums2 = [1, 4, 5]

target = 3


def searchIndex(nums, target) -> int:
    index = 0

    while index < len(nums):
        if target <= nums[index]:
            break

        index += 1

    return index


print(searchIndex(nums, target))

print(searchIndex(nums2, target))
