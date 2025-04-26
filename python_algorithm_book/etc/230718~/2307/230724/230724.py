# 정렬된 배열과 목푯값이 주어지는데 목푯값을 찾는다면 배열의 해당 인덱스를 반환하고,
# 찾지 못한다면 정렬된 배열이 되도록 목표값이 배열에 들어가야 하는 인덱스를 구하라

# 이진 탐색(해시 테이블)으로 구현한 버전

# 순차 탐색은 최악의 경우 배열 어느 값보다 가장 큰 값이 target으로 주어지면
# 모든 요소를 방문해야 하는 시간 복잡도 O(N)을 가지게 된다.

# 이진 탐색을 활용하여 시간 복잡도를 낮출 수 있다.

# 이진 탐색 : 배열의 길이가 7인 경우, 그 가운데인 4의 인덱스 요소에 먼저 접근한다.
# -> 좁혀나가기 때문에 순차 접근보다 더 적은 접근으로 원하는 값을 찾을 수 있다.

# 가운데 값을 찾는 방법:
# low = 0
# high = len(arr) - 1

# mid = (low + high) / 2

nums = [1, 2, 3, 4, 5]
target = 3


def searchInsert(nums, target) -> int:
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


print(searchInsert(nums, target))
