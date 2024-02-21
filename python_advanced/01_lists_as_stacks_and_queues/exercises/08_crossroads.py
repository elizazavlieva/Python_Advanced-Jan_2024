from collections import deque

green_light = int(input())
free_win_duration = int(input())
car_queue = deque()
counter = 0
crashed = False

command = input()
while command != 'END':
    if command != 'green':
        car_queue.append(command)
    else:
        current_green_light = green_light
        while car_queue:
            car = len(car_queue[0])
            if current_green_light == 0:
                break
            elif car <= current_green_light:
                current_green_light -= len(car_queue.popleft())
                counter += 1
            elif car > current_green_light:
                car = abs(car - current_green_light)
                if car <= free_win_duration:
                    car_queue.popleft()
                    counter += 1
                    break
                else:
                    car = abs(car - free_win_duration)
                    crashed = True
                    print(f'A crash happened!\n'
                          f'{car_queue[0]} was hit at {car_queue[0][-car]}.')
                    break
    if crashed:
        break
    command = input()

if not crashed:
    print(f'Everyone is safe.\n'
          f'{counter} total cars passed the crossroads.')