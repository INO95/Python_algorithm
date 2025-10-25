# import sys

# # 10진법 수 n을 b진법으로 출력한다.
# n, b = sys.stdin.readline().rstrip().split()
# n = int(n)
# b = int(b)  # B는 숫자로 변환해야 합니다.
# result = ""

# # 60466175 = 36의4승 + 36의3승 + 36의 2승 + 36의 1승 + 36의 0승
# # 1. n에서 b만큼 나눠줌, 나눌 수 있으면 b의 값을 별도로 문자열에 저장함
# # 2. 나누고 남은 몫을 b로 나눌 수 있으면 계속 나눠줌
# # 3. 몫이 0이 된다면 문자열의 값을 변환해서 출력함


# def int_to_char(number):
#     if 0 <= number <= 9:
#         # 0~9는 문자 '0'~'9'로 변환
#         # ord('0')을 더해서 아스키 코드로 만듦
#         return chr(ord("0") + number)
#         # 참고: 간단히 str(number)를 사용해도 됩니다.

#     elif 10 <= number <= 35:
#         # 10~35는 문자 'A'~'Z'로 변환
#         # ord('A')를 기준으로 (number - 10)만큼 더함
#         return chr(ord("A") + (number - 10))
#     else:
#         return "?"  # 예외 처리


# while True:
#     if n // b == 0:
#         result = int_to_char(n % b) + result
#         break
#     else:
#         n = n // b
#         result = int_to_char(n % b) + result
# print(result)

# 제미나이가 도와줌 ㅜ

import sys

# 10진법 수 n을 b진법으로 출력한다.
n, b = sys.stdin.readline().rstrip().split()
n = int(n)
b = int(b)  # B는 숫자로 변환해야 합니다.
result = ""


def int_to_char(number):
    if 0 <= number <= 9:
        # 0~9는 문자 '0'~'9'로 변환
        # ord('0')을 더해서 아스키 코드로 만듦
        return chr(ord("0") + number)
        # 참고: 간단히 str(number)를 사용해도 됩니다.

    elif 10 <= number <= 35:
        # 10~35는 문자 'A'~'Z'로 변환
        # ord('A')를 기준으로 (number - 10)만큼 더함
        return chr(ord("A") + (number - 10))
    else:
        return "?"  # 예외 처리


# 몫(n)이 0이 될 때까지 반복
while n > 0:
    # 1. 몫이 아닌 나머지를 구합니다.
    remainder = n % b

    # 2. 나머지를 문자로 변환합니다.
    char = int_to_char(remainder)

    # 3. 문자를 결과의 '뒤'가 아닌 '앞'에 붙입니다.
    result = char + result

    # 4. n을 몫으로 덮어써서 다음 계산을 준비합니다.
    n = n // b

print(result)
