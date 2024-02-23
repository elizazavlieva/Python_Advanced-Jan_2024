matrix = []

row, cols = [int(i) for i in input().split(', ')]
summary = 0
for row_index in range(row):
    elem_list = [int(el) for el in input().split(', ')]
    if len(elem_list) == cols:
        summary += sum(elem_list)
        matrix.append(elem_list)

print(summary)
print(matrix)
