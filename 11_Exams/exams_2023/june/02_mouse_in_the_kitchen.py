ROW, COL = [int(el) for el in input().split(',')]

matrix = []
mouse = []
cheese_positions = []

for row in range(ROW):
    matrix.append(list(input()))

    for col in range(COL):
        if matrix[row][col] == 'M':
            mouse = [row, col]

        if matrix[row][col] == 'C':
            cheese_positions.append([row, col])

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}


def checking_ranges(move):
    if move[0] in range(ROW) and move[1] in range(COL):
        return True
    return False


def movement(move, mouse, matrix, is_trapped):
    if matrix[move[0]][move[1]] == '*':
        matrix[move[0]][move[1]] = 'M'

    elif matrix[move[0]][move[1]] == 'C':
        cheese_positions.remove(move)

    elif matrix[move[0]][move[1]] == 'T':
        is_trapped = True

    if matrix[move[0]][move[1]] != '@':
        matrix[mouse[0]][mouse[1]] = '*'
        matrix[move[0]][move[1]] = 'M'
        mouse = move
    return mouse, matrix, cheese_positions, is_trapped


is_trapped = False
while True:
    command = input()

    if command == 'danger':
        if cheese_positions:
            print("Mouse will come back later!")
        break

    move = [mouse[0] + directions[command][0],
            mouse[1] + directions[command][1]]

    if checking_ranges(move):
        mouse, matrix, cheese_positions, is_trapped = movement(move, mouse, matrix, is_trapped)
        if not cheese_positions:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

        elif is_trapped:
            print('Mouse is trapped!')
            break

    else:
        print('No more cheese for tonight!')
        break

[print(*element, sep='') for element in matrix]
