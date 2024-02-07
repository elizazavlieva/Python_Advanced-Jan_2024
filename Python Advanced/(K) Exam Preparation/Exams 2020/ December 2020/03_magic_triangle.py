
def get_magic_triangle(n):
    triangle = [[1]*i for i in range(1, n + 1)]

    for row in range(2, len(triangle)):

        for col in range(1, row):

            triangle[row][col] = triangle[row - 1][col-1] + triangle[row - 1][col]

    print(triangle)


get_magic_triangle(5)
