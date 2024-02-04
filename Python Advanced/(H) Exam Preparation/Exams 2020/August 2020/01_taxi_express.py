from collections import deque

customers = deque(int(el) for el in input().split(', '))
taxi = [int(el) for el in input().split(', ')]

total_time = 0

while customers and taxi:
    if taxi[-1] >= customers[0]:
        total_time += customers.popleft()
    taxi.pop()

if customers:
    print(f'Not all customers were driven to their destinations\n'
          f'Customers left: {", ".join(str(el) for el in customers)}')
else:
    print(f'All customers were driven to their destinations\n'
          f'Total time: {total_time} minutes')
