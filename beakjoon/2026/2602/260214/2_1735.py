import sys

input = sys.stdin.readline

a_son, a_par = map(int, input().split())
b_son, b_par = map(int, input().split())

# 2/7랑 3/5의 합을 기약분수로 구하면 31/35?
# 10/35 + 21/35 = 31/35

# 분모의 최소공배수를 구한다
# 원래 분모에서 최소공배수가 되기 위한 만큼의 곱셈을 분자에도 한다
# 더하고 출력한다

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_result = a_par // gcd(a_par, b_par) * b_par

print(a_son * (gcd_result // a_par) + b_son * (gcd_result // b_par), end=" ")
print(gcd_result)

# (gpt) 기약분수로 출력 안해서 틀림

import sys
input = sys.stdin.readline

a_son, a_par = map(int, input().split())
b_son, b_par = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

lcm = a_par // gcd(a_par, b_par) * b_par

num = a_son * (lcm // a_par) + b_son * (lcm // b_par)
den = lcm

g = gcd(num, den)
print(num // g, den // g)
