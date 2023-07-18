# 230718

# 두 수의 합을 구하라

# 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목푯값을 만들 때,
# 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하라
# 입력값으로 주어지는 배열에는 정확히 하나의 정답이 존재하며,
# 같은 요소의 값을 중복해서 사용할 수 없다.

# 1. 무작정 구하기

nums = [1, 5, 2, 9, 7]
target = 8


def findTarget(nums, target) -> nums:
    for i in range(0, len(nums)):
        nums1_item = nums[i]
        for j in range(1, len(nums)):
            nums2_item = nums[j]
            if nums1_item + nums2_item == target:
                return [i, j]


print(findTarget(nums, target))
