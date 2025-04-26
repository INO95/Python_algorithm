# 정수형(int), 부동 소수형(float), 문자열(str), 불리언(bool) 의 경우에는
# 값에 의한 참조로 호출

def adder_two(a):
    a += 2

    return a


b = 2

c = adder_two(b)
print(f"b: {b}, c:{c}")

# 리스트(list), 튜플(tuple), 사전(dict) 등의 타입은 참조에 의한 호출과 동일하게 동작함


def append_element(in_list):
    in_list.append(3)


list_test = [2]
# list_test 자체가 업데이트된다.
append_element(list_test)
print(f'{list_test}')

# 일반 대입으로 이루어지는 리스트 연산은 값에 의한 호출로 처리된다.
# 즉, append_element() 함수 내에 값이 할당되는 순간 새로운 리스트를 생성하여 해당 값을 처리한다.


def append_element2(in_list2):
    in_list2 = [3, 4]


list_test2 = [2]

append_element2(list_test2)
print(f'{list_test2}')

# slice()
# 참조에 의한 대입으로 바뀌기 때문에 list_test3가 업데이트된다.


def append_element3(in_list3):
    in_list3[:] = [3, 4]


list_test3 = [2]

append_element3(list_test3)
print(f'{list_test3}')
