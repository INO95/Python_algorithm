# py_list를 1, 2, 3, 4, 5로 초기화하고 6 요소를 추가(append) 한다.
py_list = [1, 2, 3, 4, 5]
py_list.append(6)
print(py_list)

# py_list_1에 py_list_2의 [4, 5, 6]을 추가(append)한다.
py_list_1 = [1, 2, 3]
py_list_2 = [4, 5, 6]
py_list_1.append(py_list_2)
print(py_list_1)

# py_list_1에 py_list_2의 [4, 5, 6]을 확장(extend)한다.
py_list_1 = [1, 2, 3]
py_list_2 = [4, 5, 6]
py_list_1.extend(py_list_2)
print(py_list_1)

# py_list에 2의 요소를 삭제한다.
# list에는 중복된 값이 있을 수 있고, 여러 값들 중에 가장 앞선 인덱스의 요소가 삭제된다.
py_list = [1, 2, 3, 2, 4]
py_list.remove(2)
print(py_list)

# py_list의 모든 요소를 삭제한다.
py_list = [1, 2, 3]
py_list.clear()
print(py_list)

# py_list의 2번째 있는 요소를 삭제한다.
py_list = [1, 2, 3]
del py_list[1]
print(py_list)
