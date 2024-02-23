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
    print(f'Cups:', *cups_capacity)
else:
    print(f'Bottles:', *bottle_capacity)

print(f'Wasted litters of water: {wasted_water}')
