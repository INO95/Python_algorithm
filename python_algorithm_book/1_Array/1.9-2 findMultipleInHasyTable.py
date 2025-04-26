arr = [4, 5, 4, 4, 3, 1, 4, 6, 4, 7, 4, 4, 6, 4]


def majorityElement(arr) -> int:
    majority_count = int(len(arr)/2)

    # 해시맵을 선언
    hashmap = {}

    for num in arr:
        # 만약 해시맵에 해당 요소가 이미 존재한다면
        if hashmap.get(num) != None:
            # 해시맵의 value (요소의 갯수)를 1 올린다.
            hashmap[num] = hashmap[num] + 1
        # key는 배열의 요소
        # value는 배열 요소의 갯수이다.
        # 처음에는 배열의 요소 : 1 로 설정한다.
        else:
            hashmap[num] = 1

        # 만약 해시맵의 요소가 과반수 이상이 되면 return
        if hashmap[num] > majority_count:
            return num
    return -1


print(majorityElement(arr))
