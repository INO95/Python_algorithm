import sys

n, m = map(int, sys.stdin.readline().split())

pokes = {}
answers = []

for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    pokes[i] = name

reversePokes = {v: k for k, v in pokes.items()}

for _ in range(m):
    answer = str(sys.stdin.readline().rstrip())
    answers.append(answer)

for x in answers:
    if x.isdigit():
        print(pokes[int(x)])
    else:
        print(reversePokes[(x)])

# gemini feedback

import sys

# Making 'input' shorter to type
input = sys.stdin.readline

n, m = map(int, input().split())

# Create two dictionaries to look up in both directions
id_to_name = {}
name_to_id = {}

# 1. Build both maps in a single loop
for i in range(1, n + 1):
    name = input().rstrip()
    id_to_name[i] = name
    name_to_id[name] = i

# 2. Process questions immediately
for _ in range(m):
    query = input().rstrip()

    # Check if the query is a number
    if query.isdigit():
        # Query is a number -> Find the Name
        print(id_to_name[int(query)])
    else:
        # Query is a name -> Find the ID
        print(name_to_id[query])
