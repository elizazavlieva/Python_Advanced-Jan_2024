from collections import deque

ramen_bowls = [int(el) for el in input().split(', ')]
customers = deque(int(el) for el in input().split(', '))

while ramen_bowls and customers:
    if ramen_bowls[-1] == customers[0]:
        ramen_bowls.pop()
        customers.popleft()
    elif ramen_bowls[-1] > customers[0]:
        ramen_bowls[-1] -= customers.popleft()

    else:
        customers[0] -= ramen_bowls.pop()

if not customers:
    print('Great job! You served all the customers.')
    if ramen_bowls:
        print(f'Bowls of ramen left: {", ".join(str(el) for el in ramen_bowls)}')
else:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    print(f'Customers left: {", ".join(str(el) for el in customers)}')