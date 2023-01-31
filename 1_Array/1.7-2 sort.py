nums1 = [2, 8, 10, 45, 113, 350]
nums2 = [5, 7, 9, 14, 120, 243, 350]

m = 6
n = 7


def merge(nums1, nums2, m, n) -> None:
    for i, nums1_item in enumerate(nums1):
        if nums1_item > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item

            # nums2[:] = sorted(nums2)

            for k, item in enumerate(nums2[1:], start=1):
                if nums1_item <= item:
                    nums2[k - 1] = nums1_item
                    break

                nums2[k - 1] = nums2[k]
                nums2[k] = nums1_item


merge(nums1, nums2, m, n)

print(nums1)
print(nums2)
