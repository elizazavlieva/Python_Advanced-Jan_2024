from collections import deque

cups_capacity = deque(int(i) for i in input().split())
bottle_capacity = [int(i) for i in input().split()]

wasted_water = 0
while cups_capacity and bottle_capacity:
    if cups_capacity[0] <= bottle_capacity[-1]:
        wasted_water += abs(cups_capacity.popleft() - bottle_capacity.pop())
    else:
        cups_capacity[0] -= bottle_capacity.pop()

if cups_capacity:
    print('Cups:', end='')
    for i in cups_capacity:
        print(f' {i}', end='')

else:
    print('Bottles:', end='')
    for i in bottle_capacity:
        print(f' {i}', end='')

print()
print(f'Wasted litters of water: {wasted_water}')
