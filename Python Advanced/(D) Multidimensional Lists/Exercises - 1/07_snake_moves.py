from collections import deque
rows, cols = [int(el) for el in input().split()]
string = [el for el in input()]
matrix = []
index = 0
for row in range(rows):
    current_row = deque()
    for col in range(cols):
        if index == len(string):
            index = 0
        if row % 2 == 0:
            current_row.append(string[index])
        else:
            current_row.appendleft(string[index])
        index += 1
    matrix.append([''.join(current_row)])

[print(*matrix[row]) for row in range(len(matrix))]
