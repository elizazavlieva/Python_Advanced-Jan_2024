line = input()
size = int(input())
matrix = []
player = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'P':
            player = [row, col]

turns = int(input())

direction_mapper = {'up': (-1, 0), 'down': (1, 0),
                    'left': (0, -1), 'right': (0, 1)}

for _ in range(turns):
    command = input()
    move = [player[0] + direction_mapper[command][0],
            player[1] + direction_mapper[command][1]]
    if move[0] in range(size) and move[1] in range(size):
        if matrix[move[0]][move[1]] != '-':
            line += matrix[move[0]][move[1]]
        matrix[move[0]][move[1]] = 'P'
        matrix[player[0]][player[1]] = '-'
        player = move
    else:
        line = line[0:len(line) - 1]

print(line)
[print(*elements, sep='') for elements in matrix]
