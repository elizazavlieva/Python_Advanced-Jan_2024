from collections import deque

firework_effects = deque(map(int, input().split(', ')))
explosive_power = list(map(int, input().split(', ')))

fireworks_data = {'Palm': 0, 'Willow': 0, 'Crossette': 0}
made_firework = ''
task_completed = False
while firework_effects and explosive_power:

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    explosive = explosive_power.pop()
    effects = firework_effects.popleft()
    mix = explosive + effects

    if mix % 3 == 0 and mix % 5 != 0:
        made_firework = 'Palm'
        fireworks_data[made_firework] += 1

    elif mix % 5 == 0 and mix % 3 != 0:
        made_firework = 'Willow'
        fireworks_data[made_firework] += 1

    elif mix % 3 == 0 and mix % 5 == 0:
        made_firework = 'Crossette'
        fireworks_data[made_firework] += 1

    else:
        firework_effects.append(effects - 1)
        explosive_power.append(explosive)

    for values in fireworks_data.values():
        if values < 3:
            break
    else:
        task_completed = True
        break

if task_completed:
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can\'t make the perfect firework show.')

if firework_effects:
    print(f'Firework Effects left: {", ".join(map(str, firework_effects))}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(map(str, explosive_power))}')

[print(f'{firework} Fireworks: {count}') for firework, count in fireworks_data.items()]
