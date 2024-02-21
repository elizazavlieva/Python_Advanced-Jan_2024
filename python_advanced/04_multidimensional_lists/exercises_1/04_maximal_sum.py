rows, cols = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

sum_max = float('-inf')
sub_matrix = []
for row in range(rows - 2):
    for col in range(cols - 2):
        first_up = matrix[row][col]
        second_up = matrix[row][col + 1]
        third_up = matrix[row][col + 2]
        first_mid = matrix[row + 1][col]
        second_mid = matrix[row + 1][col + 1]
        third_mid = matrix[row + 1][col + 2]
        first_below = matrix[row + 2][col]
        second_below = matrix[row + 2][col + 1]
        third_below = matrix[row + 2][col + 2]
        current_sum = first_up + second_up + third_up + first_mid + \
                      second_mid + third_mid + first_below + second_below + third_below
        if sum_max < current_sum:
            sum_max = current_sum
            sub_matrix = [[first_up, second_up, third_up],
                          [first_mid, second_mid, third_mid],
                          [first_below, second_below, third_below]]
print(f'Sum = {sum_max}')
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])
