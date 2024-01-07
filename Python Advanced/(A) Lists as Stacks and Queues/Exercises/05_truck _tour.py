"""
There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive).
For each petrol pump, you will receive two pieces of information (separated by a single space):
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter
 of petrol per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so you
 can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
You never miss filling its tank at a petrol pump.
"""

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
