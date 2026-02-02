# import sys

# n = int(sys.stdin.readline())
# members = []

# for _ in range(n):
#     member, entered = sys.stdin.readline().split()
#     if entered == "leave":
#         members.remove(member)
#     else:
#         members.append(member)
# members.sort(reverse=True)
# for member in members:
#     print(member)

import sys

n = int(sys.stdin.readline())
input = sys.stdin.readline
members = {}

for _ in range(n):
    member, status = input().split()
    members[member] = status

sortedMembers = dict(sorted(members.items(), reverse=True))

for member in sortedMembers:
    if sortedMembers[member] != "leave":
        print(member)

# gemini's feedback

import sys

n = int(sys.stdin.readline())
current_members = {}

for _ in range(n):
    name, status = sys.stdin.readline().split()

    if status == "enter":
        current_members[name] = True
    else:
        # "leave" means they are gone, so remove them.
        # 'del' on a dictionary is O(1)
        del current_members[name]

# 1. Sort the keys in descending order
# 2. Since we deleted the 'leavers', everyone left is currently in the company.
for name in sorted(current_members.keys(), reverse=True):
    print(name)

# feedback 2
import sys

n = int(sys.stdin.readline())
members = set()

for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter":
        members.add(name)
    else:
        members.remove(name)

# Sort the set directly and print
for name in sorted(members, reverse=True):
    print(name)

# Both the Dictionary (`del`) and Set (`remove`) approaches are excellent. Great job recognizing the need for a Hash-based structure!
