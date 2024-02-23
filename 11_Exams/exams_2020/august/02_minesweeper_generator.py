import ast
from collections import deque

n = int(input())
bombs_num = int(input())
bomb_positions = deque(ast.literal_eval(input()) for _ in range(bombs_num))
matrix = [[0] * n for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (1, -1), (-1, 1), (1, 1)]

while bomb_positions:
    bomb = bomb_positions.popleft()

    matrix[bomb[0]][bomb[1]] = '*'

    for side in directions:
        move = [bomb[0] + side[0],
                bomb[1] + side[1]]

        if move[0] in range(n) and move[1] in range(n):
            if matrix[move[0]][move[1]] == 0:
                matrix[move[0]][move[1]] = 1

            elif matrix[move[0]][move[1]] != '*':
                matrix[move[0]][move[1]] += 1


[print(*elements) for elements in matrix]
