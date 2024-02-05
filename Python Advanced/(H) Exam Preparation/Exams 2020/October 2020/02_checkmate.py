size = 8

matrix = []
king_position = []
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'K':
            king_position = [row, col]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (1, -1), (-1, 1), (1, 1)]
queens_position = []
for rows, cols in directions:
    move = king_position

    while True:
        move = [move[0] + rows,
                move[1] + cols]

        if move[0] in range(size) and move[1] in range(size):
            if matrix[move[0]][move[1]] == 'Q':
                queens_position.append(move)
                break
        else:
            break

if queens_position:
    [print(element) for element in queens_position]
else:
    print('The king is safe!')
