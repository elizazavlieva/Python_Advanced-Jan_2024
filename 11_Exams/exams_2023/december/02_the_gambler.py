SIZE = int(input())
money = 100
matrix = []
player = []
for row in range(SIZE):
    matrix.append(list(input()))
    for col in range(SIZE):
        if matrix[row][col] == 'G':
            player = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}


def game_over(player, money):
    if player[0] not in range(SIZE) and player[1] not in range(SIZE) or money <= 0:

        return True

    return False

def movement(player, matrix, money, win=False):
    if matrix[player[0]][player[1]] == 'W':
        money += 100

    elif matrix[player[0]][player[1]] == 'P':
        money -= 200

    elif matrix[player[0]][player[1]] == 'J':
        money += 100000
        win = True

    matrix[player[0]][player[1]] = 'G'
    return money, win

def output():
    print("Game over! You lost everything!")


win = False
while True:
    command = input()
    if command == 'end':
        print(f"End of the game. Total amount: {money}$")
        break
    matrix[player[0]][player[1]] = '-'
    player = [directions[command][0] + player[0], directions[command][1] + player[1]]
    if game_over(player, money):
        output()
        break
    else:
        money, win = movement(player, matrix, money)
        if win:
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
            break
        if game_over(player, money):
            output()
            break

if not game_over(player, money):
    [print(*elements, sep='') for elements in matrix]
