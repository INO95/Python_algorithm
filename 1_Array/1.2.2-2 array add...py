# array 모듈을 arr 이름으로 사용하기
import array as arr

# int_arr 를 정수형 [1, 2, 3]을 가지도록 초기화
int_arr = arr.array('i', [1, 2, 3])

print("elements in array : ", end="")
# int_arr의 길이만큼, 인덱스 0부터 시작
for i in range(0, len(int_arr)):
    print(int_arr[i], end=" ")
print()

# 1의 위치에 4의 값을 추가
int_arr.insert(1, 4)

print("elements after insertion : ", end="")
for i in range(0, len(int_arr)):
    print(int_arr[i], end=" ")
print()

# 1 을 값을 찾아 제거
int_arr.remove(1)

# '을 표현하기 위해서 \을 붙여준다.
print("elements after delete \'1\' in array : ", end=" ")
for i in int_arr:
    print(i, end=" ")
print()
