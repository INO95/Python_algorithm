nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [4, 5, 6]
m = 3
n = 3


def merge(nums1, m, nums2, n) -> None:
    for i, v in enumerate(nums2):
        nums1[m + i] = v

    nums1[:] = sorted(nums1)


merge(nums1, m, nums2, n)

print(nums1)
