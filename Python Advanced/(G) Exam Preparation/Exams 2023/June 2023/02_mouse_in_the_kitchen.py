n, m = [int(el) for el in input().split(',')]

matrix = []
mouse = []
cheese_positions = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == 'M':
            mouse = [row, col]
        if matrix[row][col] == 'C':
            cheese_positions.append([row, col])

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}


while True:
    command = input()
    if command == 'danger':
        if cheese_positions:
            print("Mouse will come back later!")
        break
    move = [mouse[0] + directions[command][0],
            mouse[1] + directions[command][1]]
    if move[0] in range(n) and move[1] in range(m):

        if matrix[move[0]][move[1]] == '*':
            matrix[move[0]][move[1]] = 'M'
            matrix[mouse[0]][mouse[1]] = '*'
            mouse = move

        if matrix[move[0]][move[1]] == 'C':

            cheese_positions.remove(move)
            matrix[mouse[0]][mouse[1]] = '*'
            matrix[move[0]][move[1]] = 'M'
            mouse = move
            if not cheese_positions:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        if matrix[move[0]][move[1]] == 'T':

            matrix[mouse[0]][mouse[1]] = '*'
            matrix[move[0]][move[1]] = 'M'
            print('Mouse is trapped!')
            break

        if matrix[move[0]][move[1]] == '@':
            continue

    else:
        print('No more cheese for tonight!')
        break

[print(*element, sep='') for element in matrix]