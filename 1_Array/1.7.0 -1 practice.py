nums1 = [5, 3, 1]
nums2 = [2, 5, 3, 7]
m = 3
n = 4
arr1 = [0 for i in range(m)]
arr2 = [0 for i in range(n)]


def sorting(nums1, nums2, m, n) -> None:
    i = m - 1
    j = n - 1
    q = m + n - 1
    for k in range(q):
        if j - k > 0:
            if nums1[i] < nums2[j]:
                arr2[m-k] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                arr2[m-k] = nums1[i]
                i -= 1
        elif j - k <= 0 and i - k > 0:
            l = -(m + n - 1 - j) + k
            if nums1[i] < nums2[j]:
                arr1[n-k] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                arr1[n-k] = nums1[i]
                i -= 1
        else:
            nums1 = arr1
            nums2 = arr2
            break


sorting(nums1, nums2, m, n)

print(arr2, arr2)
