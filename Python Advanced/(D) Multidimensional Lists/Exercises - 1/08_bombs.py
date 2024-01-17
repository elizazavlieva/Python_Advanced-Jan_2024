from collections import deque


def bomb_explosion():
    global matrix, bomb_coordinates
    while bomb_coordinates:
        bomb_row, bomb_col = (int(i) for i in bomb_coordinates.popleft().split(","))
        if matrix[bomb_row][bomb_col] > 0:
            for loc in location:
                index_one = bomb_row + loc[0]
                index_two = bomb_col + loc[1]
                if 0 <= index_one < n and 0 <= index_two < n:
                    if matrix[index_one][index_two] > 0:
                        matrix[index_one][index_two] -= matrix[bomb_row][bomb_col]
            matrix[bomb_row][bomb_col] = 0


location = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]

n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
bomb_coordinates = deque(b for b in input().split())
bomb_explosion()
alive_cells = [num for row in range(len(matrix)) for num in matrix[row] if num > 0]
print(f'Alive cells: {len(alive_cells)}\n'
      f'Sum: {sum(alive_cells)}')
[print(*matrix[row]) for row in range(len(matrix))]

