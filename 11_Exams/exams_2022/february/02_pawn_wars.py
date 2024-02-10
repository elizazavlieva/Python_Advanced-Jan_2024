from collections import deque

SIZE = 8

ranks = {0: ["8", "a"], 1: ["7", "b"], 2: ["6", "c"], 3: ["5", "d"],
         4: ["4", "e"], 5: ["3", "f"], 6: ["2", "g"], 7: ["1", "h"]}

players = deque(['w', 'b'])

player_mapper = {"w": {"moves": (-1, 0), "diagonals": [(-1, -1), (-1, 1)]},
                 "b": {"moves": (1, 0), "diagonals": [(1, -1), (1, 1)]}}

names = {"w": "White", "b": "Black"}

board = []
players_position = {}

for row in range(SIZE):
    board.append(input().split())
    for col in range(SIZE):
        if board[row][col] == 'b' or board[row][col] == 'w':
            players_position[board[row][col]] = [row, col]


def checking_diagonals(current_position, current_player, player_mapper, board, command):
    for coords in player_mapper[current_player][command]:
        move = [current_position[0] + coords[0],
                current_position[1] + coords[1]]
        if move[0] in range(SIZE) and move[1] in range(SIZE):
            if board[move[0]][move[1]] != "-":

                return True,  move
    return False, current_position


def movement(current_player, current_position, board, player_mapper, command):
    move = [current_position[0] + player_mapper[current_player][command][0],
            current_position[1] + player_mapper[current_player][command][1]]

    board[current_position[0]][current_position[1]] = '-'
    board[move[0]][move[1]] = current_player
    return move, board


def reached_last_rank(current_player, current_position):
    if current_position[0] == 0 and current_player == 'w':
        return True
    if current_position[0] == SIZE - 1 and current_player == 'b':
        return True
    return False


win = False
while True:
    current_player = players[0]
    current_position = players_position[current_player]
    win, current_position = checking_diagonals(current_position, current_player, player_mapper, board, "diagonals")

    if win:
        square = ranks[current_position[1]][1] + ranks[current_position[0]][0]
        print(f'Game over! {names[current_player]} win, capture on {square}.')
        break

    current_position, board = movement(current_player, current_position, board, player_mapper, "moves")
    win = reached_last_rank(current_player, current_position)

    if win:
        square = ranks[current_position[1]][1] + ranks[current_position[0]][0]
        print(f'Game over! {names[current_player]} pawn is promoted to a queen at {square}.')
        break

    players_position[current_player] = current_position
    players.rotate(-1)
