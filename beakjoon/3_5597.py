import sys

students = list(range(1, 31))

for _ in range(28):
    num = int(sys.stdin.readline().rstrip())
    if num in students:
        students.remove(num)

for student in students:
    print(student)


# gemini가 제안한 방법 2가지 set 방식 vs 체크리스트 방식

# set 방식
# import sys

# # 1. 1부터 30까지의 학생 번호로 set 생성
# all_students = set(range(1, 31))

# # 2. 제출한 학생(28명)을 set에서 제거
# for _ in range(28):
#     submitted_student = int(sys.stdin.readline())
#     all_students.remove(submitted_student)

# # 3. 남은 학생들을 정렬하여 한 줄씩 출력
# # sorted()는 set을 list로 변환하여 정렬해줍니다.
# for student in sorted(all_students):
#     print(student)


# 체크리스트 방식
# import sys

# # 1. 31개의 False를 가진 리스트 생성 (인덱스 0은 사용 안 함)
# submitted = [False] * 31

# # 2. 제출한 학생 번호에 해당하는 위치를 True로 변경
# for _ in range(28):
#     num = int(sys.stdin.readline())
#     submitted[num] = True

# # 3. 1번부터 30번까지 확인하며 값이 False인 학생 번호 출력
# for i in range(1, 31):
#     if not submitted[i]: # submitted[i]가 False라면
#         print(i)
