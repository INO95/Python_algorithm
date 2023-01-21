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

arr = [4, 5, 4, 4, 3, 1, 4, 6, 4, 7, 4, 4, 6, 4]


def majorityElement(arr) -> int:
    majority_count = int(len(arr)/2)

    for i, item_i in enumerate(arr):
        count = 0
        for j, item_j in enumerate(arr[i:], start=i):
            if item_i == item_j:
                count += 1
            if count > majority_count:
                return item_i

    return -1


print(majorityElement(arr))
