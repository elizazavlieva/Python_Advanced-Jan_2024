from collections import deque

monster = deque(int(el) for el in input().split(','))
striking_impact = [int(el) for el in input().split(',')]
killed_monsters = 0

while monster and striking_impact:
    if striking_impact[-1] >= monster[0]:
        remaining_impact = striking_impact.pop() - monster.popleft()
        killed_monsters += 1

        if len(striking_impact) >= 1 and remaining_impact > 0:
            striking_impact[-1] += remaining_impact
        elif not striking_impact and remaining_impact > 0:
            striking_impact.append(remaining_impact)

    else:
        monster[0] -= striking_impact.pop()
        monster.rotate(-1)

if not monster:
    print('All monsters have been killed!')
if not striking_impact:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {killed_monsters}')
