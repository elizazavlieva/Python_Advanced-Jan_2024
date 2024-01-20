n = int(input())
matrix = []
collected_tea = 0
left_wonderland = False
ready_for_party = False
alice_position = ()
for row in range(n):
    elements = input().split()
    for col in range(len(elements)):
        if elements[col] == 'A':
            alice_position = (row, col)
            break
    matrix.append(elements)


while True:
    matrix[alice_position[0]][alice_position[1]] = '*'
    if left_wonderland or ready_for_party:
        break
    command = input()
    move = ()
    if command == 'down':
        move = (alice_position[0] + 1, alice_position[1])
    elif command == 'up':
        move = (alice_position[0] - 1, alice_position[1])
    elif command == 'left':
        move = (alice_position[0], alice_position[1] - 1)
    elif command == 'right':
        move = (alice_position[0], alice_position[1] + 1)
    if 0 <= move[0] < len(matrix) and 0 <= move[1] < len(matrix):
        if matrix[move[0]][move[1]] == 'R':
            left_wonderland = True
        elif matrix[move[0]][move[1]].isdigit():
            collected_tea += int(matrix[move[0]][move[1]])

            if collected_tea >= 10:
                ready_for_party = True

        alice_position = move

    else:
        left_wonderland = True

if left_wonderland:
    print('Alice didn\'t make it to the tea party.')
else:
    print('She did it! She went to the party.')

[print(*elements) for elements in matrix]
