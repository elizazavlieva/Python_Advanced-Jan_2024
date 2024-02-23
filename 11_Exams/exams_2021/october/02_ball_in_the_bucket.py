import ast
import sys

size = 6
matrix = [[el for el in input().split()] for _ in range(size)]


def sum_column(col, matrix, size):
    summary = 0
    for row in range(size):
        if matrix[row][col] != 'B':
            summary += int(matrix[row][col])

    return summary


result = 0
for _ in range(3):
    coords = ast.literal_eval(input())

    try:
        if matrix[coords[0]][coords[1]] == 'B':
            result += sum_column(coords[1], matrix, size)
            matrix[coords[0]][coords[1]] = '-'

    except (IndexError, ValueError):
        continue


prize_info = {'Football': (100, 199), 'Teddy Bear': (200, 299),
              'Lego Construction Set': (300, sys.maxsize)}

diff = sys.maxsize
for prize, ranges in prize_info.items():
    if result in range(ranges[0], ranges[1] + 1):
        print(f'Good job! You scored {result} points, and you\'ve won {prize}.')
        break

    if ranges[0] - result < diff:
        diff = ranges[0] - result

else:
    print(f'Sorry! You need {diff} points more to win a prize.')
