n = int(input())
money = 100
matrix = []
player = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'G':
            player = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}
game_over = False

while True:
    command = input()
    if command == 'end':
        print(f"End of the game. Total amount: {money}$")
        break
    move = [directions[command][0] + player[0], directions[command][1] + player[1]]
    if move[0] not in range(n) and move[1] not in range(n):
        game_over = True
        break
    else:
        if matrix[move[0]][move[1]] == 'W':
            money += 100
        elif matrix[move[0]][move[1]] == 'P':
            money -= 200

            if money <= 0:
                game_over = True
                break
        elif matrix[move[0]][move[1]] == 'J':
            money += 100000
            matrix[player[0]][player[1]] = '-'
            matrix[move[0]][move[1]] = 'G'
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
            break
        matrix[player[0]][player[1]] = '-'
        matrix[move[0]][move[1]] = 'G'
        player = move

if game_over:
    print("Game over! You lost everything!")

else:
    [print(*elements, sep='') for elements in matrix]