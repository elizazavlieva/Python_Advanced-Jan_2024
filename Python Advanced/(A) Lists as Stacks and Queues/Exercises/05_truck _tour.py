from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    petrol, distance = input().split()
    pumps.append([int(petrol), int(distance)])
start_position = 0
stops = 0
while stops < n:
    fuel = 0
    for i in range(n):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        else:
            stops += 1
            fuel -= destination

print(start_position)
