nums = [3, 2, 5, 1, 4, 0]


def missingNumber(nums) -> int:
    # set 선언
    # set 은 집합을 의미하며 순서가 없고 중복을 허용하지 않는다.
    set_nums = set(nums)

    # i는 0부터 len(nums) - 1 까지 움직이기 때문에
    # + 1을 해줘야 할 필요가 있다.
    for i in range(len(nums) + 1):
        if i not in set_nums:
            return i
    return -1


print(missingNumber(nums))
