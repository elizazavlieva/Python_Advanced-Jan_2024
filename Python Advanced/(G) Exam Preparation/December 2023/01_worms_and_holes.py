from collections import deque

worms = [int(el) for el in input().split()]
worms_count = len(worms)
holes = deque(int(el) for el in input().split())
counter = 0

while worms and holes:
    worm = worms[-1]
    hole = holes[0]
    if worms[-1] == holes[0]:
        worms.pop()
        counter += 1
    else:
        worms[-1] -= 3
    holes.popleft()
    if worms and worms[-1] <= 0:
        worms.pop()

if counter:
    print(f'Matches: {counter}')
else:
    print('There are no matches.')
if counter == worms_count:
    print('Every worm found a suitable hole!')
elif not worms and counter > 0:
    print('Worms left: none')
elif worms:
    print(f'Worms left: {", ".join(str(el) for el in worms)}')
else:
    print('Worms left: none')


if holes:
    print(f'Holes left: {", ".join(str(el) for el in holes)}')
else:
    print('Holes left: none')