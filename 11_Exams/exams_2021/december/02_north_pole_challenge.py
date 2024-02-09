ROWS, COLS = map(int, input().split(", "))
matrix = []
player = []
christmas_items = []
for row in range(ROWS):
    matrix.append(input().split())
    for col in range(COLS):
        if matrix[row][col] == "Y":
            player = [row, col]
        if matrix[row][col] in ["C", "D", "G"]:
            christmas_items.append([row, col])

direction_mapper = {"up": (-1, 0), "down": (1, 0),
                    "left": (0, -1), "right": (0, 1)}

collected_items = {"D": [0, "Christmas decorations"],
                   "G": [0, "Gifts"], "C": [0, "Cookies"]}


def movement(player, side, direction_mapper):
    move = [player[0] + direction_mapper[side][0],
            player[1] + direction_mapper[side][1]]
    if move[0] in range(ROWS) and move[1] in range(COLS):
        return move
    else:
        if move[0] < 0:
            move[0] = ROWS - 1
        if move[1] < 0:
            move[1]  = COLS - 1
        if move[0] >= ROWS:
            move[0] = 0
        if move[1] >= COLS:
            move[1] = 0
        return move


is_all_collected = False
command = input()
while command != "End":
    side, step = command.split("-")

    for i in range(int(step)):
        matrix[player[0]][player[1]] = 'x'
        player = movement(player, side, direction_mapper)
        item = matrix[player[0]][player[1]]

        if item == "D" or item == "G" or item == "C":
            collected_items[item][0] += 1
            christmas_items.remove(player)
        matrix[player[0]][player[1]] = 'Y'

        if not christmas_items:
            is_all_collected = True
            break

    if is_all_collected:
        print("Merry Christmas!")
        break

    command = input()

print("You've collected:")
[print(f"- {count} {items}") for count, items in collected_items.values()]
[print(*elements, sep=" ") for elements in matrix]