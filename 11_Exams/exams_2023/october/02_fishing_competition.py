SIZE = int(input())
matrix = []
sailor = []

for row in range(SIZE):
    matrix.append(list(input()))
    for col in range(SIZE):
        if matrix[row][col] == 'S':
            sailor = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

collected_fish = 0
sink = False
reached_quota = False


def movement(directions, command, sailor):
    sailor = [directions[command][0] + sailor[0],
              directions[command][1] + sailor[1]]
    if sailor[0] not in range(SIZE) or sailor[1] not in range(SIZE):

        for pos in range(2):
            if sailor[pos] < 0:
                sailor[pos] = SIZE - 1
            elif sailor[pos] >= SIZE:
                sailor[pos] = 0
    return sailor


command = input()
while command != 'collect the nets':
    matrix[sailor[0]][sailor[1]] = '-'
    sailor = movement(directions, command, sailor)

    if matrix[sailor[0]][sailor[1]].isnumeric():
        collected_fish += int(matrix[sailor[0]][sailor[1]])

        if collected_fish >= 20:
            reached_quota = True

    elif matrix[sailor[0]][sailor[1]] == 'W':
        sink = True
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{sailor[0]},{sailor[1]}]')
        break

    matrix[sailor[0]][sailor[1]] = 'S'

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
