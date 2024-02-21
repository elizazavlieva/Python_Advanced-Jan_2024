ROWS, COLS = [int(el) for el in input().split()]

matrix = []
start_position = []
for row in range(ROWS):
    matrix.append(list(input()))
    for col in range(COLS):
        if matrix[row][col] == 'B':
            start_position = [row, col]

current_pos = start_position
directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}


def checking_ranges(move):
    if move[0] in range(ROWS) and move[1] in range(COLS):
        return True
    return False


def movement(move, matrix, current_pos, delivered):
    if matrix[move[0]][move[1]] == 'P':
        matrix[move[0]][move[1]] = 'R'
        print('Pizza is collected. 10 minutes for delivery.')

    elif matrix[move[0]][move[1]] == 'A':
        matrix[move[0]][move[1]] = 'P'
        delivered = True
        print('Pizza is delivered on time! Next order...')

    elif matrix[move[0]][move[1]] == '-':
        matrix[move[0]][move[1]] = '.'

    if matrix[move[0]][move[1]] != '*':
        current_pos = move

    return matrix, current_pos, delivered


delivered = False
in_range = True
command = input()
while True:
    move = [current_pos[0] + directions[command][0],
            current_pos[1] + directions[command][1]]

    if checking_ranges(move):
        matrix, current_pos, delivered = movement(move, matrix, current_pos, delivered)
        if delivered:
            break
    else:
        print('The delivery is late. Order is canceled.')
        matrix[start_position[0]][start_position[1]] = " "
        break

    command = input()

[print(*elements, sep="") for elements in matrix]