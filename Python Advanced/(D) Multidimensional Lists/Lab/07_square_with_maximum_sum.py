import sys

rows, cols = [int(el) for el in input().split(', ')]
sub_matrix = []
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
max_sum = float('-inf')
for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
