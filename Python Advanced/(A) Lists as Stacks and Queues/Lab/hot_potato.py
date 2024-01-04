"""
Hot Potato is a game in which children form a circle and toss a hot potato.
The counting starts with the first kid. Every nth toss, the child holding the potato leaves the game.
When a kid leaves the game, it passes the potato to the next kid. It continues until there is only one kid left.
Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names,
separated by a single space. On the second line, you will receive the nth toss (integer)
in which a child leaves the game.
"""

from collections import deque
kids_names = deque(input().split())
toss = int(input())


while len(kids_names) != 1:
    kids_names.rotate(-toss + 1)
    print(f'Removed {kids_names.popleft()}')

print(f'Last is {kids_names[0]}')
