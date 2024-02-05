n = int(input())
matrix = []
sailor = []

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'S':
            sailor = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

collected_fish = 0
sink = False
reached_quota = False

command = input()
while command != 'collect the nets':

    position = [directions[command][0] + sailor[0], directions[command][1] + sailor[1]]
    if position[0] not in range(n) or position[1] not in range(n):

        for pos in range(2):
            if position[pos] < 0:
                position[pos] = n - 1
            elif position[pos] >= n:
                position[pos] = 0

    if matrix[position[0]][position[1]].isnumeric():

        collected_fish += int(matrix[position[0]][position[1]])
        if collected_fish >= 20:
            reached_quota = True

    elif matrix[position[0]][position[1]] == 'W':

        sink = True
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{position[0]},{position[1]}]')

        break

    matrix[sailor[0]][sailor[1]] = '-'
    matrix[position[0]][position[1]] = 'S'
    sailor = [position[0], position[1]]
    command = input()

if not sink:

    if not reached_quota:
        print(f'You didn\'t catch enough fish and didn\'t reach the quota! '
              f'You need {abs(collected_fish - 20)} tons of fish more.')
    else:
        print('Success! You managed to reach the quota!')

    if collected_fish > 0:
        print(f'Amount of fish caught: {collected_fish} tons.')
    [print(*element, sep='') for element in matrix]
