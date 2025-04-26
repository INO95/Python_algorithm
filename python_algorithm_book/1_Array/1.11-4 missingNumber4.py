nums = [3, 2, 6, 1, 4, 0]


def missingNumber(nums) -> int:
    expected_sum = 0
    nums_sum = 0

    for i in range(len(nums) + 1):
        # 정상적인 배열일 경우에 총합값
        expected_sum += i

    for _, num in enumerate(nums):
        # 현재 배열의 총합값
        nums_sum += num

    # 둘의 차는 자연스럽게 비어있는 요소의 element가 된다.
    return expected_sum - nums_sum


print(missingNumber(nums))


def missingNumber2(nums) -> int:
    # 가우스 덧셈을 활용한 리팩터링 1
    expected_sum = int((len(nums) * (len(nums) + 1)) / 2)
    nums_sum = 0
    for _, num in enumerate(nums):
        nums_sum += num
    return expected_sum - nums_sum


print(missingNumber2(nums))


def missingNumber3(nums) -> int:
    # sum 함수를 활용한 리팩터링 2
    return int((len(nums) * (len(nums) + 1)) / 2) - sum(nums)


print(missingNumber3(nums))
