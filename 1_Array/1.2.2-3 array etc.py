import array as arr

int_list = [1, 2, 3, 4, 3, 6, 7, 4, 5, 10]

# list의 요소를 배열로 변환
int_arr = arr.array('i', int_list)

print("elements in array : ")
for i in (int_arr):
    print(i, end=" ")
print()

# 3의 값이 가장 처음 나타나는 배열의 인덱스를 출력
print("The index of 1st occurrence of 3 is : ", end="")
print(int_arr.index(3))
print("The index of 1st occurrence of 1 is : ", end="")
print(int_arr.index(1))

# 배열 4번째 요소의 값을 5로 업데이트
int_arr[4] = 5
print("elements after updation : ", end="")
for i in (int_arr):
    print(i, end=" ")
print()
