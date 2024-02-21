from collections import deque

customers = deque()

command = input()
while command != 'End':
    if command == 'Paid':
        while customers:
            print(customers.pop())
    else:
        customers.appendleft(command)
    command = input()

print(f'{len(customers)} people remaining.')
