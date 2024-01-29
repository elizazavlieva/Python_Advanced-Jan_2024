rows, cols = [int(el) for el in input().split(' ')]
matrix = []
start_position = tuple()

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'B':
            start_position = (row, col)


directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

delivery_pos = [start_position[0], start_position[1]]


while True:
    command = input()
    if not  command:
        break
    move = [delivery_pos[0] + directions[command][0],
            delivery_pos[1] + directions[command][1]]
    if move[0] in range(rows) and move[1] in range(cols):
        if matrix[move[0]][move[1]] == '*':
            continue
        if matrix[move[0]][move[1]] == 'P':
            delivery_pos = move
            matrix[move[0]][move[1]] = 'R'
            print('Pizza is collected. 10 minutes for delivery.')

        if matrix[move[0]][move[1]] == 'A':
            delivery_pos = move
            matrix[move[0]][move[1]] = 'P'
            print('Pizza is delivered on time! Next order...')
            break
        if matrix[move[0]][move[1]] == '-':
            delivery_pos = move
            matrix[delivery_pos[0]][delivery_pos[1]] = '.'

    else:
        print('The delivery is late. Order is canceled.')
        matrix[start_position[0]][start_position[1]] = ' '
        break


[print(*element, sep='') for element in matrix]