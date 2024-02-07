rows,cols = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

command = input().split()
while command[0] != 'END':
    if command[0] == 'swap' and len(command) == 5:
        row_index_one = int(command[1])
        col_index_one = int(command[2])
        row_index_two = int(command[3])
        col_index_two = int(command[4])
        if ((0 > col_index_one or col_index_one >= cols) or (0 > col_index_two or col_index_two >= cols)) or (
                (0 > row_index_one or row_index_one >= rows) or (0 > row_index_two or row_index_two >= rows)):
            print('Invalid input!')
        else:
            matrix[row_index_one][col_index_one], matrix[row_index_two][col_index_two] = \
                matrix[row_index_two][col_index_two], matrix[row_index_one][col_index_one]
            for i in range(rows):
                print(" ".join([el for el in matrix[i]]))
    else:
        print('Invalid input!')

    command = input().split()
