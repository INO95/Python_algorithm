# 정렬된 배열의 정합 2

# 정렬된 배열 nums1, nums2가 주어지고, 각각의 크기는 m과 n이다.
# 정렬을 유지하면서 nums1 배열부터 채워나가 nums2까지 확장해보자.

# m + n 크기만큼의 공간은 있지 않다

# nums1 배열에 nums1과 nums2의 모든 요소를 작은 수부터 채워나가고
# nums2에는 나머지를 정렬을 유지하면서 넣도록 하자

# 추가 배열 할당 없이 문제를 해결해야 한다 (공간 복잡도 O(1))

nums1 = [2, 6, 8, 9]
nums2 = [1, 3]
m = 4
n = 2


def merge(nums1, nums2):
    for i, nums1_item in enumerate(nums1):
        if nums1_item > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item

            # 배열 2의 정렬
            for k, item in enumerate(nums2[1:], start=1):
                if nums1_item <= item:
                    nums2[k - 1] = nums1_item
                    break
                nums2[k - 1] = nums2[k]
                nums2[k] = nums1_item


merge(nums1, nums2)
print(nums1)
print(nums2)
