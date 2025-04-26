# 선형 순회
# 목푯값이 정렬된 배열 안에 있으면 그 위치를 반환하고
# 배열 안에 없다면 목푯값이 배열에서
# 위치하기 적절한 곳의 인덱스를 반환한다.
nums = [1, 2, 3, 4, 5]

nums2 = [1, 4, 5]

target = 3


def searchIndex(nums, target) -> int:
    index = 0

    while index < len(nums):
        # 목푯값이 배열의 수보다 작거나 같으면 반환
        if target <= nums[index]:
            break

        # 목푯갑시 배열의 수보다 크다면 인덱스 1 증가
        index += 1

    # break 혹은 최종 값을 반환
    return index


print(searchIndex(nums, target))

print(searchIndex(nums2, target))
