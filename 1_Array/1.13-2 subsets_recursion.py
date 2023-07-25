# 부분집합 구하기
# 재귀함수 이용

# 완전히 이해하진 못한 듯 하다.

nums = [1, 2, 3]
# 부분집합을 구하여 담을 배열
res = []
# 부분집합 하나 하나를 담을 배열
sub = []
index = 0


def subsets_recursion(nums, res, sub, index) -> None:
    # 재귀함수의 종료조건
    if len(sub) > len(nums):
        return res

    # sub 배열을 res에 append
    # 참조에 의한 호출을 위한 copy() 함수 이용
    res.append(sub.copy())

    for i in range(index, len(nums)):
        # 부분집합에 append
        sub.append(nums[i])
        subsets_recursion(nums, res, sub, i + 1)
        # 재귀를 탈출하면서 pop
        sub.pop()


subsets_recursion(nums, res, sub, index)

print(res)
