from collections import deque

bomb_effects = deque(int(el) for el in input().split(', '))
bomb_casings = [int(el) for el in input().split(', ')]

bombs_info = {'Datura Bombs': [40, 0], 'Cherry Bombs': [60, 0], 'Smoke Decoy Bombs': [120, 0]}
created_bombs = set()
task_completed = False
while bomb_casings and bomb_effects:
    result = bomb_casings[-1] + bomb_effects[0]
    for bomb, value in bombs_info.items():
        if result == value[0]:
            bombs_info[bomb][1] += 1
            created_bombs.add(bomb)
            bomb_casings.pop()
            bomb_effects.popleft()
            break
    else:
        bomb_casings[-1] -= 5
    for values in bombs_info.values():
        if values[1] < 3:
            break
    else:
        task_completed = True
        print('Bene! You have successfully filled the bomb pouch!')
        break

else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if bomb_effects:
    print(f'Bomb Effects: {", ".join(str(el) for el in bomb_effects)}')
else:
    print('Bomb Effects: empty')
if bomb_casings:
    print(f'Bomb Casings: {", ".join(str(el) for el in bomb_casings)}')
else:
    print('Bomb Casings: empty')

for bomb, value in sorted(bombs_info.items(), key= lambda kvp: kvp[0]):
    print(f'{bomb}: {value[1]}')
