from collections import deque

food_qty = int(input())
queue = deque([int(num) for num in input().split()])
print(max(queue))

while queue and food_qty >= queue[0]:
    food_qty -= queue[0]
    queue.popleft()

if queue:
    print('Orders left:', *queue)
else:
    print('Orders complete')
