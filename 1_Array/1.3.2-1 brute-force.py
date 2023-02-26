# 배열 중에서 두 수의 합이 target과 같아지는 항목의 인덱스를 찾아라.

nums = [2, 7, 8, 11]
target = 9


def twoSum(nums, target) -> nums:
    # 전체 순환
    for i in range(0, len(nums)):
        # 하나를 고르고 나머지 부분 순환
        for j in range(i + 1, len(nums)):
            # 합이 target이면 리턴
            if (nums[i] + nums[j]) is target:
                return [i, j]
            return [-1, -1]


print(twoSum(nums, target))
