import ast
from collections import deque

size = 7
players = deque(input().split(', '))
players_points = {players[0]: [501, 0], players[-1]: [501, 0]}

matrix = [[el for el in input().split()] for _ in range(size)]
winner = ''

coords = ast.literal_eval(input())
while coords:
    current_player = players[0]
    players_points[current_player][1] += 1

    if coords[0] in range(size) and coords[1] in range(size):
        if matrix[coords[0]][coords[1]].isdigit():
            players_points[current_player][0] -= int(matrix[coords[0]][coords[1]])

        elif matrix[coords[0]][coords[1]] == 'B':
            winner = current_player

            break

        else:
            left, right = int(matrix[coords[0]][0]), int(matrix[coords[0]][size - 1])
            up, down = int(matrix[0][coords[1]]), int(matrix[size-1][coords[1]])

            if matrix[coords[0]][coords[1]] == 'D':
                players_points[current_player][0] -= (left + right + up + down) * 2
            elif matrix[coords[0]][coords[1]] == 'T':
                players_points[current_player][0] -= (left + right + up + down) * 3

        if players_points[current_player][0] <= 0:
            winner = current_player

            break
    players.rotate(-1)
    coords = ast.literal_eval(input())

print(f'{winner} won the game with {players_points[winner][1]} throws!')