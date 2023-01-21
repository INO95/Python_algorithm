nums = [3, 4, 2, 6, 5]

k = 2


def rotate(nums, k) -> None:
    count = 0

    for start in range(len(nums)):
        if count >= len(nums):
            break

        curr_index = start
        prev_elem = nums[start]

        while True:
            next_index = (curr_index + k) % len(nums)
            temp = nums[next_index]
            nums[next_index] = prev_elem
            prev_elem = temp

            curr_index = next_index
            count += 1

            if curr_index == start:
                break


rotate(nums, k)

print(nums)
