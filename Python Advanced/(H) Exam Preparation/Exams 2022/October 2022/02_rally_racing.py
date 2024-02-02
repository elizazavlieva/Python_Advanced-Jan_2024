size = int(input())
racing_num = input()

matrix = []
car_position = [0, 0]
tunnel_positions = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'T':
            tunnel_positions.append([row, col])

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

passed_km = 0


while True:
    command = input()
    if command == 'End':
        matrix[car_position[0]][car_position[1]] = 'C'
        print(f'Racing car {racing_num} DNF.')
        break

    move = [directions[command][0] + car_position[0],
            directions[command][1] + car_position[1]]

    if matrix[move[0]][move[1]] == 'T':

        passed_km += 30
        tunnel_positions.remove(move)
        tunnel_move = tunnel_positions.pop()
        matrix[car_position[0]][car_position[1]] = '.'
        matrix[move[0]][move[1]] = '.'
        car_position = tunnel_move

    elif matrix[move[0]][move[1]] == 'F':

        passed_km += 10
        matrix[move[0]][move[1]] = 'C'
        matrix[car_position[0]][car_position[1]] = '.'
        car_position = move
        print(f'Racing car {racing_num} finished the stage!')
        break

    else:
        passed_km += 10
        matrix[car_position[0]][car_position[1]] = '.'
        car_position = move


print(f'Distance covered {passed_km} km.')

[print(*element, sep='') for element in matrix]