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

# gemini

# Read all 5 numbers in one line
numbers = [int(sys.stdin.readline()) for _ in range(5)]

# Sort them
numbers.sort()

# Calculate and Print
print(sum(numbers) // 5)  # sum() does the addition for you
print(numbers[2])
