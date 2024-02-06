from collections import deque

pizza_orders = deque(int(el) for el in input().split(', '))
employees = [int(el) for el in input().split(', ')]

completed_orders = 0
separated_order = 0
while pizza_orders and employees:
    if pizza_orders[0] > 10 or pizza_orders[0] <= 0:
        pizza_orders.popleft()
        continue
    if pizza_orders[0] <= employees[-1]:
        if separated_order == 0:
            completed_orders += pizza_orders.popleft()
        else:
            completed_orders += separated_order
            separated_order = 0
            pizza_orders.popleft()
        employees.pop()

    else:
        separated_order = pizza_orders[0]
        pizza_orders[0] -= employees.pop()

if not pizza_orders:
    print(f'All orders are successfully completed!\n'
          f'Total pizzas made: {completed_orders}')
    if employees:
        print(f'Employees: {", ".join(map(str, employees))}')
else:
    print(f'Not all orders are completed.\n'
          f'Orders left: {", ".join(map(str, pizza_orders))}')
