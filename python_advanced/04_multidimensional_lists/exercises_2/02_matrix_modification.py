n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

command = input().split()
while command[0] != "END":
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if command[0] == 'Add':
            matrix[row][col] += value
        elif command[0] == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    command = input().split()

[print(*elements) for elements in matrix]