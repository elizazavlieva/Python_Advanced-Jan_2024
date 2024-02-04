
n = int(input())
matrix = []
snake = []
burrow = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'S':
            snake = [row, col]
        elif matrix[row][col] == 'B':
            burrow.append([row, col])


directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

food_qnty = 0

command = input()
while command:
    move = [snake[0] + directions[command][0],
            snake[1] + directions[command][1]]

    if move[0] in range(n) and move[1] in range(n):
        if matrix[move[0]][move[1]] == '*':
            food_qnty += 1
            matrix[snake[0]][snake[1]] = '.'
            matrix[move[0]][move[1]] = 'S'
            snake = move
            if food_qnty >= 10:
                print(f'You won! You fed the snake.')
                break
        elif matrix[move[0]][move[1]] == 'B':
            burrow.remove(move)
            matrix[move[0]][move[1]] = '.'
            matrix[snake[0]][snake[1]] = '.'
            snake = burrow.pop()
            matrix[snake[0]][snake[1]] = 'S'

        else:
            matrix[snake[0]][snake[1]] = '.'
            matrix[move[0]][move[1]] = 'S'
            snake = move


    else:
        matrix[snake[0]][snake[1]] = '.'
        print("Game over!")
        break

    command = input()

print(f'Food eaten: {food_qnty}')

[print(*elements, sep='') for elements in matrix]