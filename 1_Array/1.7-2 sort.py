# 두 배열의 요소를 병합 후 정렬한다.
# 단, 추가적인 배열을 생성하지 않는 조건 하에.

nums1 = [2, 8, 10, 45, 113, 350]
nums2 = [5, 7, 9, 14, 120, 243, 350]
# 각 배열의 길이
m = 6
n = 7


def merge(nums1, nums2, m, n) -> None:
    # 배열 1의 요소를 enumerate 한다.
    for i, nums1_item in enumerate(nums1):
        # 배열 1의 요소가 배열 2의 첫 번째 요소보다 크면
        if nums1_item > nums2[0]:
            # 배열 1의 요소와 배열 2의 첫 번째 요소를 교환한다.
            # 즉, 베열 1부터 작은 순서대로 정렬한다.
            nums1[i] = nums2[0]
            nums2[0] = nums1_item

            # nums2[:] = sorted(nums2)

            # 배열 2의 두 번째 요소부터 loop
            for k, item in enumerate(nums2[1:], start=1):
                # 배열 2의 두 번째 요소가 첫 번째 요소보다 클 경우
                if nums1_item <= item:
                    nums2[k - 1] = nums1_item
                    break

                # 배열 2의 두 번째 요소가 첫 번째 요소보다 작을 경우
                # 배열 2의 첫 번째, 두 번째 요소를 변경한다.
                nums2[k - 1] = nums2[k]
                nums2[k] = nums1_item


merge(nums1, nums2, m, n)

print(nums1)
print(nums2)
