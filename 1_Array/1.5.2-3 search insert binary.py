# 이진 순회

nums = [1, 2, 3, 4, 5]

nums2 = [1, 4, 5]

# test case 1
target2 = 0

# test case 2
target3 = 100

target = 3


def searchIndex(nums, target) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low


print(searchIndex(nums, target))

print(searchIndex(nums2, target))

print(searchIndex(nums, target2))

print(searchIndex(nums, target3))
