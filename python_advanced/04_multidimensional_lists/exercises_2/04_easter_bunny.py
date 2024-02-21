size = int(input())

bunny_position = []
matrix = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_position = [row, col]
            break


possible_directions = {'up': (-1, 0), 'down': (1, 0),
                       'left': (0, -1), 'right': (0, 1)}
possible_moves = []
score = float('-inf')
move = ''

for k, v in possible_directions.items():
    r = v[0]
    c = v[1]
    new_row = bunny_position[0] + r
    new_col = bunny_position[1] + c
    current_score = 0
    current_moves = []
    while new_row in range(size) and new_col in range(size):
        if matrix[new_row][new_col] == 'X':
            break

        current_score += int(matrix[new_row][new_col])
        current_moves.append([new_row, new_col])
        new_row += r
        new_col += c

    if current_score > score and current_moves:
        score = current_score
        possible_moves = current_moves
        move = k

print(move)
[print(i) for i in possible_moves]
print(score)