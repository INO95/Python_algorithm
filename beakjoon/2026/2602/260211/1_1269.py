import sys

input = sys.stdin.readline

a, b = map(int, input().split())
a_str = set(input().split())
b_str = set(input().split())

a_b = a_str.difference(b_str)
b_a = b_str.difference(a_str)

print(len(a_b) + len(b_a))

# Gpt advice 1

import sys
input = sys.stdin.readline

input()
A = set(input().split())
B = set(input().split())

print(len(A ^ B))


