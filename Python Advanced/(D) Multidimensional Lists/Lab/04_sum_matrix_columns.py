rows, cols = [int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for col in range(cols):
    summary = 0
    for row in range(rows):
        summary += matrix[row][col]
    print(summary)
