n, m = [int(el) for el in input().split()]
matrix = []
player = []
touched_opponents = 0
for row in range(n):
    matrix.append(input().split())
    for col in range(m):
        if matrix[row][col] == 'B':
            player = [row, col]


directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}
counter = 0
win = False

command = input()
while command != 'Finish':
    move = [player[0] + directions[command][0],
            player[1] + directions[command][1]]
    if move[0]  in range(n) and move[1]  in range(m):
        if matrix[move[0]][move[1]] == 'P':
            touched_opponents += 1
            counter += 1
            matrix[move[0]][move[1]] = 'B'
            matrix[player[0]][player[1]] = '-'
            player = move
            if touched_opponents == 3:
                break
        elif matrix[move[0]][move[1]] == '-':
            counter += 1
            matrix[move[0]][move[1]] = 'B'
            matrix[player[0]][player[1]] = '-'
            player = move

    command = input()

print(f'Game over!\n'
      f'Touched opponents: {touched_opponents} Moves made: {counter}')