from collections import deque

size = 6

matrix = []
rover = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'E':
            rover = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

deposits = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}

commands = deque(el for el in input().split(', '))

while commands:
    side = commands.popleft()
    rover = [rover[0] + directions[side][0],
             rover[1] + directions[side][1]]

    if rover[0] not in range(size) or rover[1] not in range(size):
        for i in range(2):
            if rover[i] >= size:
                rover[i] = 0
            if rover[i] < 0:
                rover[i] = size - 1

    if matrix[rover[0]][rover[1]] in ['W', 'M', 'C']:
        symbol = matrix[rover[0]][rover[1]]
        print(f'{deposits[symbol][0]} deposit found at ({rover[0]}, {rover[1]})')
        deposits[symbol][1] += 1
    elif matrix[rover[0]][rover[1]] == 'R':
        print(f'Rover got broken at ({rover[0]}, {rover[1]})')
        break

for elements, count in deposits.items():
    if count[1] == 0:
        print('Area not suitable to start the colony.')
        break
else:
    print(f'Area suitable to start the colony.')
