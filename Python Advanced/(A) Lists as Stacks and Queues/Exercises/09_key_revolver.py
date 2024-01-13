from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(i) for i in input().split()]
locks = deque(int(i) for i in input().split())
intelligence_value = int(input())

reloading = barrel_size
bullet_counter = 0

while bullets and locks:
    if bullets and reloading == 0:
        print('Reloading!')
        reloading = barrel_size
    if bullets[-1] <= locks[0]:
        print('Bang!')
        bullets.pop()
        locks.popleft()
    else:
        print('Ping!')
        bullets.pop()
    bullet_counter += 1
    reloading -= 1

if bullets and reloading == 0:
    print('Reloading!')

if locks:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
else:
    print(f'{len(bullets)} bullets left. Earned ${intelligence_value - (bullet_counter * bullet_price)} ')