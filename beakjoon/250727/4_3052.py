import sys

num_list = set()

for _ in range(10):
    num = int(sys.stdin.readline())
    num_list.add(num % 42)

print(len(num_list))

# gemini의 개선 방안

# import sys

# # Set comprehension을 사용해 10개의 입력을 받아 42로 나눈 나머지를 바로 set에 저장
# remainders = {int(sys.stdin.readline()) % 42 for _ in range(10)}

# print(len(remainders))
