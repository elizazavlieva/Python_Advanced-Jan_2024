n = int(input())
matrix = []
knight_positions = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'K':
            knight_positions.append([row, col])

removed_knights = 0

possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                  (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hit = 0
    hit_knight = []
    for row_k, col_k in knight_positions:
        current_hit = 0
        for move in possible_moves:
            new_row = row_k + move[0]
            new_col = col_k + move[1]
            if new_row in range(n) and new_col in range(n):
                if matrix[new_row][new_col] == 'K':
                    current_hit += 1
        if current_hit > max_hit:
            max_hit = current_hit
            hit_knight = [row_k, col_k]

    if max_hit == 0:
        break
    knight_positions.remove(hit_knight)
    matrix[hit_knight[0]][hit_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)
