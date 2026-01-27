import sys

n = int(sys.stdin.readline())

listA = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in listA:
        listA.append(word)

sortedListA = sorted(listA, key=lambda x: (len(x), x))

for x in sortedListA:
    print(x)

# gemini's feedback
import sys

n = int(sys.stdin.readline())

# 1. Use a set to automatically remove duplicates while reading
#    (List Comprehension + set)
word_set = set(sys.stdin.readline().rstrip() for _ in range(n))

# 2. Convert back to a list to sort
word_list = list(word_set)

# 3. Sort using your perfect lambda logic
#    First by length (len(x)), then alphabetically (x)
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)
