# 230719

# 두 수의 합을 구하라

# 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목푯값을 만들 때,
# 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하라
# 입력값으로 주어지는 배열에는 정확히 하나의 정답이 존재하며,
# 같은 요소의 값을 중복해서 사용할 수 없다.

# 2. hash table을 이용해보기

nums = [1, 5, 2, 9, 7]
target = 8


def twoSum(nums, target) -> int:
    # 해시 테이블 생성
    hashtable_dict = {}
    # 해시 테이블 순회
    # 0부터 길이만큼
    for i in range(0, len(nums)):
        # target에서 해시 테이블의 요소를 뺀 값
        value = target - nums[i]
        # 만약 해시 테이블에 이미 value 가 존재한다면
        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
            return sorted([i, hashtable_dict[value]])
        # 존재하지 않는다면 해시테이블에 해당 데이터 추가 (키 : 배열의 밸류, 값 : 배열의 인덱스)
        hashtable_dict[nums[i]] = i
    # 없는 경우
    return [-1. - 1]


print(twoSum(nums, target))
