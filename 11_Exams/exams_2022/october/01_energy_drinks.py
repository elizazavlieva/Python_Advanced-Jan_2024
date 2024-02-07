from collections import deque


caffeine_ml = [int(el) for el in input().split(', ')]
energy_drinks = deque(int(el) for el in input().split(', '))
max_caffeine = 300
total_caffeine = 0

while caffeine_ml and energy_drinks:
    current_caffeine = caffeine_ml[-1] * energy_drinks[0]

    if (current_caffeine + total_caffeine) > max_caffeine:
        energy_drinks.rotate(-1)
        total_caffeine -= 30

        if total_caffeine < 0:
            total_caffeine = 0

    else:
        total_caffeine += current_caffeine
        energy_drinks.popleft()

    caffeine_ml.pop()

if energy_drinks:
    print(f'Drinks left: {", ".join(str(el) for el in energy_drinks)}')

else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')