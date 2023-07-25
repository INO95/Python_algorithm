# arr = [4, 5, 4, 4, 3, 1, 4, 6, 4, 7, 4, 4, 6, 4]

# 1 1 2 3 3 3 3 3 4

# def find(arr):

#     a = 0
#     b = 0
#     c = 0
#     d = 0

#     for i in range(arr):

#         sorted(arr)

#         if(i == 0):
#             a += 1
#             c = arr[i]

#         if(arr[i] == arr[i+1]):
#             a += 1
#             c = arr[i]

#         elif(arr[i] < arr[i+1]):
#             b += 1
#             d = arr[i]


# print(find(arr))


# 배열 중 과반수 이상의 중복된 요소가 있으면 그 요소를 return
arr = [4, 5, 4, 4, 3, 1, 4, 6, 4, 7, 4, 4, 6, 4]


def majorityElement(arr) -> int:
    # 과반수를 설정
    majority_count = int(len(arr)/2)

    for i, item_i in enumerate(arr):
        count = 0
        # 배열을 하나 복사하고 enumerate
        for j, item_j in enumerate(arr[i:], start=i):
            # 두 같은 배열을 놓고 같은 요소가 있으면 count를 올린다.
            if item_i == item_j:
                count += 1
            # 만약 현재 참조중인 요소의 수가 과반수 이상이 되면 그 수를 return
            if count > majority_count:
                return item_i

    return -1


print(majorityElement(arr))
