import ast
from collections import deque

player = deque(input().split(', '))
matrix = [[el for el in input().split()] for _ in range(6)]

resting_player = {'Tom': False, 'Jerry': False}
skip_turn = {'Tom': False, 'Jerry': False}

while True:
    position = [el for el in ast.literal_eval(input())]
    current_player = player[0]

    if resting_player[current_player] and not skip_turn[current_player]:
        skip_turn[current_player] = True
        player.rotate(-1)
        continue

    else:
        skip_turn[current_player] = False
        resting_player[current_player] = False

    if matrix[position[0]][position[1]] == 'E':
        print(f'{current_player} found the Exit and wins the game!')
        break

    elif matrix[position[0]][position[1]] == 'T':
        print(f'{current_player} is out of the game! The winner is {player[-1]}.')
        break

    elif matrix[position[0]][position[1]] == 'W':
        print(f'{current_player} hits a wall and needs to rest.')
        resting_player[current_player] = True

    player.rotate(-1)
