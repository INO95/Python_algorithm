nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    count = 0

    for start in range(len(nums)):
        # count가 배열의 길이 이상이 되면 break
        if count >= len(nums):
            break

        # curr_index의 초깃값은 0으로 한다.
        curr_index = start
        # prev_elem 의 초깃값은 원 배열의 첫번 째 요소로 한다.
        prev_elem = nums[start]

        while True:
            # 다음에 업데이트할 배열 요소의 인덱스
            # 처음에는 0과 k의 거리만큼 떨어져 있는 인덱스다.
            next_index = (curr_index + k) % len(nums)
            # 업데이트 될 요소를 업데이트 전에 미리 임시 저장한다.
            temp = nums[next_index]
            # 미리 저장해두었던 이전 element를 업데이트한다.
            nums[next_index] = prev_elem
            # 미리 임시 저장한 temp를 prev_elem에 저장한다.
            prev_elem = temp
            # 다음에 수행할 인덱스를 curr_index에 업데이트한다.
            curr_index = next_index
            # count를 증가
            count += 1
            # 배열의 길이만큼 수행하면 마지막에는 처음 수행했던 인덱스로 돌아온다.
            if curr_index == start:
                break


rotate(nums, k)

print(nums)
