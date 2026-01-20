import sys

numbers = []
num_sum = 0
num_avg = 0
for _ in range(5):
    num = int(sys.stdin.readline())
    numbers.append(num)
    num_sum = num_sum + num
num_avg = num_sum // 5
numbers.sort()

print(num_avg)
print(numbers[2])
