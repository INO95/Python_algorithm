# 이진 순회

nums = [1, 2, 3, 4, 5]

nums2 = [1, 4, 5]

target = 3

# test case 1
target2 = 0

# test case 2
target3 = 100


def searchIndex(nums, target) -> int:
    # low, high를 지정한다.
    low = 0
    # 배열은 0부터 시작하기 때문에 1을 제한다.
    high = len(nums) - 1

    # low가 high보다 작은 경우에
    while low <= high:
        # 중간값
        mid = int((low + high) / 2)

        # 목푯값과 중간값(인덱스)의 값이 같으면 return
        if target == nums[mid]:
            return mid
        # 목푯값이 더 크다면 low를 중간값에서 1을 더한 수치로 변환
        if target > nums[mid]:
            low = mid + 1
        # 목푯값이 더 작다면 high를 중간값에서 1을 더한 수치로 변환
        else:
            high = mid - 1
    # 목푯값이 가장 작았던 경우
    return low


print(searchIndex(nums, target))

print(searchIndex(nums2, target))

print(searchIndex(nums, target2))

print(searchIndex(nums, target3))
