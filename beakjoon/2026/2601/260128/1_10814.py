# import sys

# n = int(sys.stdin.readline())

# members = []

# for i in range(n):
#     age, name = sys.stdin.readline().split()
#     members.append([age, name, i + 1])

# members.sort(key=lambda x: (x[0], x[2]))

# for member in members:
#     print(member[0], member[1])

# gemini's feedback
import sys

n = int(sys.stdin.readline())

members = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    # Fix: Convert age to int immediately!
    members.append([int(age), name, i + 1])

# Now it compares integers (9 < 10), so it works correctly.
members.sort(key=lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])

# feedback 2
import sys

n = int(sys.stdin.readline())
members = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    # Convert age to int
    members.append([int(age), name])

# Python's sort is stable.
# If ages are equal, it preserves the original order automatically.
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])
