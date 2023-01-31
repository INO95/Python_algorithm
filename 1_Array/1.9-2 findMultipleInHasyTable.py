arr = [4, 5, 4, 4, 3, 1, 4, 6, 4, 7, 4, 4, 6, 4]


def majorityElement(arr) -> int:
    majority_count = int(len(arr)/2)

    hashmap = {}

    for num in arr:
        if hashmap.get(num) != None:
            hashmap[num] = hashmap[num] + 1
        else:
            hashmap[num] = 1

        if hashmap[num] > majority_count:
            return num
    return -1


print(majorityElement(arr))
