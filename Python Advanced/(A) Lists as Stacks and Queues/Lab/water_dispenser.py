"""
On the first line, you will receive the starting quantity of water (integer) in a dispenser.
Then, on the following lines, you will be given the names of some people who want to get water
(each on a separate line) until you receive the command "Start".
Add those people to a queue. Finally, you will receive some commands until the command "End":
-	"{liters}" - litters (integer) that the current person in the queue wants to get.
Check if there is enough water in the dispenser for that person.
        If there is enough water, print "{person_name} got water" and remove
            him/her from the queue.
        Otherwise, print "{person_name} must wait" and remove the
            person from the queue without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left".
"""

from collections import deque

water_qty = int(input())
line = deque()

while True:
    command = input()
    if command == 'Start':
        break
    line.append(command)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'refill':
        water_qty += int(command[1])
    else:
        water = int(command[0])
        if water <= water_qty:
            water_qty -= water
            print(f"{line.popleft()} got water")
        else:
            print(f'{line.popleft()} must wait')
print(f'{water_qty} liters left')
