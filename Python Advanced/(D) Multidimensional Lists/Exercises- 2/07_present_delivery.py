def cookie():
    global santa, command, nice_kids, presents, count_nice_kids, matrix
    for key, value in directions.items():
        m_row = santa[0] + value[0]
        m_col = santa[1] + value[1]
        if m_row in range(size) and m_col in range(size) and presents > 0:
            if matrix[m_row][m_col] == 'V':
                matrix[m_row][m_col] = '-'
                nice_kids -= 1
                presents -= 1
                count_nice_kids += 1
            elif matrix[m_row][m_col] == 'X':
                matrix[m_row][m_col] = '-'
                presents -= 1


def movement():
    global santa, command, nice_kids, presents, count_nice_kids, matrix

    r = santa[0] + directions[command][0]
    c = santa[1] + directions[command][1]
    if r in range(size) and c in range(size):
        if matrix[r][c] == 'V':
            matrix[r][c] = 'S'
            matrix[santa[0]][santa[1]] = '-'
            santa = [r, c]
            nice_kids -= 1
            presents -= 1
            count_nice_kids += 1
        elif matrix[r][c] == 'C':
            matrix[r][c] = 'S'
            matrix[santa[0]][santa[1]] = '-'
            santa = [r, c]
            cookie()
        else:
            matrix[r][c] = 'S'
            matrix[santa[0]][santa[1]] = '-'
            santa = [r, c]


presents = int(input())
size = int(input())
matrix = []
santa = []
nice_kids = 0
count_nice_kids = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'S':
            santa = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids += 1
directions = {'up': (-1, 0), 'down': (1, 0),
              'left': (0, -1), 'right': (0, 1)}

command = input()
while command != 'Christmas morning':
    movement()
    if presents == 0:
        break
    command = input()
if presents == 0 and nice_kids > 0:
    print('Santa ran out of presents!')
[print(*elements) for elements in matrix]

if nice_kids > 0:
    print(f'No presents for {nice_kids} nice kid/s.')
else:
    print(f'Good job, Santa! {count_nice_kids} happy nice kid/s.')
