rows = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
flattened = [num for sublist in matrix for num in sublist]

print(flattened)
