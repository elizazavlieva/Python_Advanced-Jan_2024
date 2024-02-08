def get_magic_triangle(n):
    triangle = []
    for row in range(n):
        triangle.append([])
        triangle[row].append(1)
        for col in range(1, row):
            result = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle[row].append(result)
        if row != 0:
            triangle[row].append(1)
    return triangle


'''TEST'''
print(get_magic_triangle(5))
