from collections import deque

water_qty = int(input())
line = deque()

while True:
    command = input()
    if command == 'Start':
        break
    line.append(command)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'refill':
        water_qty += int(command[1])
    else:
        water = int(command[0])
        if water <= water_qty:
            water_qty -= water
            print(f"{line.popleft()} got water")
        else:
            print(f'{line.popleft()} must wait')
print(f'{water_qty} liters left')
