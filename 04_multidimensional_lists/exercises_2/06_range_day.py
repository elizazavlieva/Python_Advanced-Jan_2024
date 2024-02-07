size = 5
matrix = []
player_position = []
targets = 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            player_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

direction = {'up': (-1, 0), 'down': (1, 0),
             'left': (0, -1), 'right': (0, 1)}

hit_target_position = []

n = int(input())
for _ in range(n):
    user_input = input().split()
    command, side = user_input[0], user_input[1]
    if command == 'move':
        steps = int(user_input[2])
        m_row, m_col = 0, 0
        if side == 'up':
            m_row, m_col = player_position[0] - steps, player_position[1]
        elif side == 'down':
            m_row, m_col = player_position[0] + steps, player_position[1]
        elif side == 'left':
            m_row, m_col = player_position[0], player_position[1] - steps
        elif side == 'right':
            m_row, m_col = player_position[0], player_position[1] + steps
        if m_row in range(size) and m_col in range(size) and matrix[m_row][m_col] == '.':
            matrix[m_row][m_col] = 'A'
            matrix[player_position[0]][player_position[1]] = '.'
            player_position = [m_row, m_col]

    elif command == 'shoot':
        s_row = player_position[0] + direction[side][0]
        s_col = player_position[1] + direction[side][1]
        while s_row in range(size) and s_col in range(size):
            if matrix[s_row][s_col] == 'x':
                matrix[s_row][s_col] = '.'
                targets -= 1
                hit_target_position.append([s_row, s_col])
                break
            s_row += direction[side][0]
            s_col += direction[side][1]
        if targets == 0:
            print(f'Training completed! All {len(hit_target_position)} targets hit.')
            break

if targets > 0:
    print(f'Training not completed! {targets} targets left.')

[print(elements) for elements in hit_target_position]
