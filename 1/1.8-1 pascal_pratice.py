pyramid = []

for i in range(5):
    column = []
    while i >= 0:
        column.append(0)
        i -= 1
    pyramid.append(column)

print(pyramid)
