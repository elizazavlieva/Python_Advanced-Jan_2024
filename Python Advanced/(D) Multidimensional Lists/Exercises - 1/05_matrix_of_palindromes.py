rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    elements = []
    for col in range(cols):
        characters = chr(97+row) + chr(97 + col+row) + chr(97 + row)
        elements.append(characters)
    matrix.append(elements)
    print(' '.join(matrix[row]))

