from collections import deque

chocolate_stack = [int(i) for i in input().split(', ')]
milk_cups = deque(int(i) for i in input().split(', '))
counter = 0

while chocolate_stack and milk_cups and counter < 5:
    if chocolate_stack[-1] <= 0 or milk_cups[0] <= 0:
        if chocolate_stack[-1] <= 0:
            chocolate_stack.pop()
        if milk_cups[0] <= 0:
            milk_cups.popleft()

    else:
        if milk_cups[0] == chocolate_stack[-1]:
            counter += 1
            milk_cups.popleft()
            chocolate_stack.pop()
        else:
            milk_cups.rotate(-1)
            chocolate_stack[-1] -= 5

if counter == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolate_stack:
    print(f'Chocolate: {", ".join([str(i) for i in chocolate_stack])}')
else:
    print('Chocolate: empty')
if milk_cups:
    print(f'Milk: {", ".join([str(i) for i in milk_cups])}')
else:
    print('Milk: empty')
