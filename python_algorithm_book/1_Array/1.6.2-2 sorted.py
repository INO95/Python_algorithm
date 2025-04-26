# 배열 1, 2를 정렬하여 병합하고 배열1을 반환한다.
# 배열 1에는 2가 들어갈만한 공간이 있음
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [4, 5, 6]
# 배열 2의 길이
m = 3


def merge(nums1, m, nums2) -> None:
    # enumerate를 사용하여 index, value의 형태로 loop한다.
    for i, v in enumerate(nums2):
        # 배열 2의 길이 + index
        nums1[m + i] = v

    # 참조에 의한 호출로 처리하기 위해서 slice() 사용
    nums1[:] = sorted(nums1)


merge(nums1, m, nums2)

print(nums1)
