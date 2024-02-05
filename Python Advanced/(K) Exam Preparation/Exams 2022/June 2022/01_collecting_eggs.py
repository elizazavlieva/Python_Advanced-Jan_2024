from collections import deque

egg_size = deque(int(el) for el in input().split(', '))
paper_size = deque(int(el) for el in input().split(', '))

filled_boxes = 0

while egg_size and paper_size:
    if egg_size[0] <= 0:
        egg_size.popleft()
        continue

    if egg_size[0] == 13:
        egg_size.popleft()
        first = paper_size.popleft()
        paper_size.rotate(1)
        paper_size.append(first)
        continue

    result = egg_size.popleft() + paper_size.pop()

    if result <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')

else:
    print('Sorry! You couldn\'t fill any boxes!')

if egg_size:
    print(f'Eggs left: {", ".join(str(el) for el in egg_size)}')

if paper_size:
    print(f'Pieces of paper left: {", ".join(str(el) for el in paper_size)}')
