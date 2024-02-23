n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
summary = 0
for col in range(n):
    summary += matrix[col][col]
print(summary)

