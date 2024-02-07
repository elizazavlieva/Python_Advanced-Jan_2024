import math


def movement(player, move, direction, n):
    player = [player[0] + direction[move][0],
              player[1] + direction[move][1]]
    if player[0] in range(n) and player[1] in range(n):
        return player
    else:
        for i in range(2):
            if player[i] < 0:
                player[i] = n - 1
            elif player[i] >= n:
                player[i] = 0
        return player


size = int(input())
matrix = []
player = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'P':
            player = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

command = input()
total_coins = 0
player_path = [player]
while command:
    if command in directions.keys():
        matrix[player[0]][player[1]] = '-'
        player = movement(player, command, directions, size)
        player_path.append(player)
        value = matrix[player[0]][player[1]]

        if value == 'X':
            total_coins = math.floor(total_coins / 2)
            print(f'Game over! You\'ve collected {total_coins} coins.')
            break

        elif value.isdigit():
            total_coins += int(value)

            if total_coins >= 100:
                print(f'You won! You\'ve collected {total_coins} coins.')
                break
    command = input()

print('Your path:')
[print(el) for el in player_path]
