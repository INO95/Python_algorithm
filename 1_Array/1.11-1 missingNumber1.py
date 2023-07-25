nums = [3, 2, 6, 1, 4, 0]


def missingNumber(nums) -> int:
    # 정렬
    nums.sort()

    # 마지막 요소가 배열의 길이와 같지 않다면
    # 즉, 마지막 요소가 missingNumber라면
    if nums[-1] != len(nums):
        return len(nums)
    # 첫 번째 요소가 0이 아니라면
    # 즉, 첫 번째 요소가 missingNumber라면
    if nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        # 예상 숫자와 실제 숫자를 비교한다.
        # 예상 숫자는 1부터 시작하는 수열
        expected = nums[i - 1] + 1
        if expected != nums[i]:
            return expected


print(missingNumber(nums))
