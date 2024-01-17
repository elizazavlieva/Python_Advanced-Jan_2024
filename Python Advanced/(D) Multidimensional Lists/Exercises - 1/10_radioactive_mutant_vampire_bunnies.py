def bunny_lair(matrix):
    for row in range(rows):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'P':
                return row, col


def player_movement(move):
    global matrix, won, dead, player_position
    player_move = ()
    if move == 'R':
        player_move = (player_position[0], player_position[1] + 1)
    elif move == 'L':
        player_move = (player_position[0], player_position[1] - 1)
    elif move == 'U':
        player_move = (player_position[0] - 1, player_position[1])
    elif move == 'D':
        player_move = (player_position[0] + 1, player_position[1])
    if 0 <= player_move[0] < rows and 0 <= player_move[1] < cols:
        if matrix[player_move[0]][player_move[1]] == 'B':
            dead = True
        else:
            matrix[player_move[0]][player_move[1]] = 'P'
            matrix[player_position[0]][player_position[1]] = '.'
        player_position = player_move

    else:
        won = True
        matrix[player_position[0]][player_position[1]] = '.'


def bunny_movement():
    global matrix, bunny_positions, dead
    bunny_positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'B':
                bunny_positions.append((row, col))

    for bunny in bunny_positions:
        location = [(bunny[0] - 1, bunny[1]), (bunny[0] + 1, bunny[1]),
                    (bunny[0], bunny[1] + 1), (bunny[0], bunny[1] - 1)]

        for loc in location:
            if 0 <= loc[0] < rows and 0 <= loc[1] < cols:
                if matrix[loc[0]][loc[1]] == 'P':
                    dead = True
                matrix[loc[0]][loc[1]] = 'B'


rows, cols = [int(el) for el in input().split()]
matrix = [list(input()) for _ in range(rows)]
moves = [i for i in input()]
player_position = bunny_lair(matrix)
bunny_positions = []

won = False
dead = False

for el in moves:
    player_movement(el)
    bunny_movement()
    if won or dead:
        break

if dead:
    for row in matrix:
        print(*row, sep="")
    print("dead: ", end='')
    print(*player_position, sep=' ')
else:
    for row in matrix:
        print(*row, sep="")
    print("won: ", end='')
    print(*player_position, sep=' ')
