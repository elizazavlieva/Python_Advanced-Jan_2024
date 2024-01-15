n = int(input())
matrix = [[char for char in input()] for _ in range(n)]
symbol = input()
is_existing = False

for row in range(n):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            print((row, col))
            is_existing = True
            break
    if is_existing:
        break
else:
    print(f'{symbol} does not occur in the matrix')
