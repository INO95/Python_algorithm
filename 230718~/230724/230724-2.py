# 주어진 정렬된 두 배열을 정렬을 유지하면서 병합해보자

# 배열 nums1, nums2의 각각의 크기는 m개와 n개의 요소로 초기화되어 있다.
# nums1은 nums1, nums2를 병합하기에 충분한 크기로 할당되어 있다. (m + n 개)

nums1 = [1, 2, 4, 6, 7, 0, 0, 0, 0]
nums2 = [3, 5, 8, 9]
m = 5
n = 4


def makeArray(nums1, nums2, m, n):
    index = 0
    for i in range(0, len(nums1)):
        if (i > n):
            nums1[i] = nums2[index]
            index += 1

    return sorted(nums1)

# print(makeArray(nums1, nums2, m, n))


# enumerate : 리스트를 인자로 받아 인덱스와 값을 반환해준다. (0, 1), (1, 2)...
# 파이썬에서 리스트를 변환할 때는 슬라이드 대입을 사용한다.
def makeArrayByEnumerate(nums1, nums2, m, n):
    for i, v in enumerate(nums2):
        nums1[m + i] = v
    nums1[:] = sorted(nums1)

# makeArrayByEnumerate(nums1, nums2, m, n)
# print(nums1)


def makeArray2(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


makeArray2(nums1, nums2, m, n)

print(nums1)
