nums = [0, 0, 1, 1, 1, 2, 3, 3, 4, 5]

# 중복을 제거했을 때의 배열의 길이를 구하기
# 배열을 반환하는 것이 아닌 배열의 길이만 알 수 있으면 된다.
# 즉, 기존 배열을 수정 할 필요가 없고
# count를 이용해서 그 수치만 반환하면 된다.


def removeDuplicates(nums) -> int:
    # 만약 배열의 길이가 0이거나 0보다 작다면 길이는 0
    if len(nums) <= 0:
        return 0

    # 초기치 할당
    curr = nums[0]
    # 최소 길이 1
    cnt = 1

    # nums[0]을 할당했기 때문에 nums[1]부터 비교해야 한다.
    # 그래서 인덱스 0이 아닌 1부터 시작
    for i in range(1, len(nums)):
        # 만약 수치가 다르다면 (= 중복이 아니라면)
        if curr != nums[i]:
            # 현재 값을 curr에 업데이트
            curr = nums[i]
            # 문제 조건 중 중복 제거 후 그대로 배열을 수정하라는
            # 문구가 있기 때문에 들어간 코드
            # 중복을 제거했을 때의 배열이 순차적으로 수정된다.
            nums[cnt] = curr
            print(nums)
            # count 1 증가
            cnt += 1

    # 전체 순환 이후에 cnt 반환
    return cnt


print(removeDuplicates(nums))
