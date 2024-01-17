def miner_location():
    for row in range(n):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 's':
                return row, col


def coal_location():
    position = []
    for row in range(n):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'c':
                position.append((row, col))
    return position

def miner_movement(move):
    global matrix, collected_coals, miner_position, game_over, coals
    next_move = ()
    if move == 'left':
        next_move = (miner_position[0], miner_position[1] - 1)
    elif move == 'right':
        next_move = (miner_position[0], miner_position[1] + 1)
    elif move == 'up':
        next_move = [miner_position[0] - 1, miner_position[1]]
    elif move == 'down':
        next_move = [miner_position[0] + 1, miner_position[1]]

    if 0 <= next_move[0] < n and 0 <= next_move[1] < n:
        if matrix[next_move[0]][next_move[1]] != 'e':
            if matrix[next_move[0]][next_move[1]] == 'c':
                collected_coals += 1
                coals = (next_move[0], next_move[1])

            matrix[next_move[0]][next_move[1]] = 's'
            matrix[miner_position[0]][miner_position[1]] = '*'
            miner_position = next_move
        else:
            game_over = True
            miner_position = next_move

n = int(input())
command = [el for el in input().split()]
matrix = [[el for el in input().split()] for _ in range(n)]
miner_position = miner_location()
coals_position = coal_location()
coals = []
collected_coals = 0
game_over = False

for el in command:
    miner_movement(el)
    for el in coals_position:
        if el == coals:
            coals_position.remove(coals)
    if not coals_position:
        print(f'You collected all coal! ({miner_position[0]}, {miner_position[1]})')
        break
    elif game_over:
        print(f'Game over! ({miner_position[0]}, {miner_position[1]})')
        break

else:
    print(f'{len(coals_position)} pieces of coal left. ({miner_position[0]}, {miner_position[1]})')
