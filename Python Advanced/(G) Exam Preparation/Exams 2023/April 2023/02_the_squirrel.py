from collections import deque

size = int(input())
commands = deque(input().split(', '))
matrix = []
squirrel_position = []
hazelnut_positions = []
collected_nuts = 0
for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 's':
            squirrel_position = [row, col]
        if matrix[row][col] == 'h':
            hazelnut_positions.append([row, col])


directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}
game_over = False
while commands:
    side = commands.popleft()
    move = [squirrel_position[0] + directions[side][0],
            squirrel_position[1] + directions[side][1]]
    if move[0] in range(size) and move[1] in range(size):
        if matrix[move[0]][move[1]] == 'h':

            collected_nuts += 1
            hazelnut_positions.remove(move)

        elif matrix[move[0]][move[1]] == 't':
            print('Unfortunately, the squirrel stepped on a trap...')
            game_over = True
            break

        matrix[move[0]][move[1]] = 's'
        matrix[squirrel_position[0]][squirrel_position[1]] = '*'
        squirrel_position = move

        if not hazelnut_positions:
            break
    else:
        print('The squirrel is out of the field.')
        game_over = True
        break

if hazelnut_positions and not game_over:
    print('There are more hazelnuts to collect.')
elif not game_over:
    print('Good job! You have collected all hazelnuts!')
print(f'Hazelnuts collected: {collected_nuts}')
