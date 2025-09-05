import sys

whiteChesses = sys.stdin.readline().rstrip().split()
chesses = [1, 1, 2, 2, 2, 8]

for i in range(len(chesses)):
    if i == 5:
        print(int(chesses[i]) - int(whiteChesses[i]))
    else:
        print(int(chesses[i]) - int(whiteChesses[i]), end=" ")


# 더 나은 방법 1
import sys

# 정답 피스 개수
correct_pieces = [1, 1, 2, 2, 2, 8]

# 입력을 받아 공백으로 나눈 뒤, 각 항목을 정수로 변환하여 리스트로 저장
my_pieces = list(map(int, sys.stdin.readline().split()))

result = []
# 두 리스트를 비교하여 필요한 피스 개수 계산
for i in range(len(correct_pieces)):
    result.append(correct_pieces[i] - my_pieces[i])

# 리스트 앞에 *를 붙이면 모든 요소를 공백으로 구분하여 출력해 줍니다.
print(*result)


# 더 나은 방법 2

import sys

correct_pieces = [1, 1, 2, 2, 2, 8]
my_pieces = list(map(int, sys.stdin.readline().split()))

# for 반복문을 한 줄로 압축하여 result 리스트 생성
result = [correct_pieces[i] - my_pieces[i] for i in range(len(correct_pieces))]

print(*result)
