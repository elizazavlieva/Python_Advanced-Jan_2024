from collections import deque


class FullColumnError(Exception):
    pass


rows = 6
cols = 7
max_connections = 4
direction_mapper = {
    'up': (-1, 0),
    'left': (0, -1),
    'main_diagonal': (-1, -1),
    'right_diagonal': (-1, 1)
}


def travel_direction(coordinates, current_row, current_col, element, sign, matrix):
    count = 0

    row_direction, col_direction = coordinates
    for i in range(1, max_connections + 1):
        next_row = eval(f"{current_row} {sign} {row_direction} * {i}")
        next_col = eval(f"{current_col} {sign} {col_direction} * {i}")

        try:
            if matrix[next_row][next_col] == element:
                count += 1

            else:
                return count

        except IndexError:
            return count



def is_winner(current_row, current_col, matrix):
    for direction, coords in direction_mapper.items():
        searched_element = matrix[current_row][current_col]
        win_position_count = travel_direction(coords, current_row, current_col, searched_element,"+", matrix)
        opposite_win_position_count = travel_direction(coords, current_row, current_col, searched_element, "-", matrix)
        print(opposite_win_position_count + win_position_count)
        if win_position_count + opposite_win_position_count + 1 >= max_connections:
            return True
    else:
        return False

def print_board(matrix):
    for row in matrix:
        print(row)


def validate_column_choice(col):
    return col in range(cols)


def place_player_choice(col_index, matrix):
    for row_index in range(rows - 1, -1, -1):
        if matrix[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError('This column is full, please select another column!')


def is_matrix_full(matrix):
    free_space = [el for el in matrix[0] if el == 0]
    if not free_space:
        return True
    return False


matrix = [[0 for _ in range(cols)] for _ in range(rows)]

players = deque([1, 2])

while True:
    player = players[0]

    try:
        column = input(f'Player {player} please select column: ')
        column_index = int(column) - 1
        validate_column_choice(int(column))
        row_index = place_player_choice(column_index, matrix)
        matrix[row_index][column_index] = player
        if is_winner(row_index, column_index, matrix):
            break
        if is_matrix_full(matrix):
            print('Board is full')
            exit(0)
    except FullColumnError:
        print('This column is full, please select another one!')
        continue

    except (IndexError, ValueError):
        print(f'This column is invalid, please select number between 1 and {cols}')
        continue

    print_board(matrix)
    players.rotate(-1)

print_board(matrix)
print(f' Winner is {players[0]}')
