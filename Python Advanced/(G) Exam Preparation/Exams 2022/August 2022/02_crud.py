import ast

matrix = [[el for el in input().split()] for _ in range(6)]
position = [el for el in ast.literal_eval(input())]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

line = input().split(', ')
while line[0] != 'Stop':
    command, direction = line[0], line[1]
    position = [position[0] + directions[direction][0],
                position[1] + directions[direction][1]]

    if command == 'Create':
        value = line[2]

        if matrix[position[0]][position[1]] == '.':
            matrix[position[0]][position[1]] = value

    elif command == 'Update':
        value = line[2]

        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = value

    elif command == 'Delete':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = '.'

    elif command == 'Read':
        if matrix[position[0]][position[1]] != '.':
            print(matrix[position[0]][position[1]])

    line = input().split(', ')

[print(*elements, sep=' ') for elements in matrix]