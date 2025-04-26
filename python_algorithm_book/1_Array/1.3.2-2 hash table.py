nums = [2, 7, 8, 11]
target = 9


def twoSum(nums, target) -> nums:
    # 해시테이블 선언
    hashtable_dict = {}
    for i in range(0, len(nums)):
        # 해시 테이블의 value : 목표 값의 인덱스
        # 해시 테이블의 key : 목표 값

        # 여기서의 value는 목푯값에서 현재 값을 뺀 값
        # 즉, value가 0이 되면 조건이 일치한다.
        value = target - nums[i]
        # 저장하다가 조건에 일치하면 인덱스를 반환한다.
        # 해시테이블에 value를 가지고 있는 key가 있다면
        # 그 key의 value(인덱스)가 현재 참조중인 i가 아닐 때
        # -> 원 배열에서 각 다른 항목인 것을 증명하기 위해서?
        if hashtable_dict.get(value) is not None \
                and hashtable_dict[value] != i:
            print(hashtable_dict[value])
            return sorted([i, hashtable_dict[value]])

        # 해시테이블[목표 값] : 인덱스   <- 이 형태로 저장해나간다.
        hashtable_dict[nums[i]] = i

    return [-1, -1]


print(twoSum(nums, target))
