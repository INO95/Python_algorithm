# array 모듈을 사용할 것이며, 해당 모듈은 arr이라는 이름으로 접근하도록 하겠다.
import array as arr

# 정수형 배열을 생성하고 초깃값으로 [1, 2, 3]을 가진다.
int_array = arr.array('i', [1, 2, 3])
print(int_array)
