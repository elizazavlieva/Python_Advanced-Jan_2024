size = int(input())
matrix = []
submarine = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'S':
            submarine = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}
destroyed_cruisers = 0
mines = 0
command = input()
while command:
    move = [submarine[0] + directions[command][0],
            submarine[1] + directions[command][1]
            ]
    if matrix[move[0]][move[1]] == 'C':
        destroyed_cruisers += 1

    elif matrix[move[0]][move[1]] == '*':
        mines += 1
    matrix[submarine[0]][submarine[1]] = '-'
    matrix[move[0]][move[1]] = 'S'
    submarine = move
    if destroyed_cruisers == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    if mines == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
        break
    command = input()

[print(*elements, sep='') for elements in matrix]