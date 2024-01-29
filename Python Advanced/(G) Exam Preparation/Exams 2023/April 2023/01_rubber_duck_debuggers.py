from collections import deque

time = deque(int(el) for el in input().split())
tasks = [int(el) for el in input().split()]

rubber_ducks_info = {'Darth Vader Ducky': 0, 'Thor Ducky': 0,
                     'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

ducky_type = {'Darth Vader Ducky': (0, 60), 'Thor Ducky': (61, 120),
              'Big Blue Rubber Ducky': (121, 180), 'Small Yellow Rubber Ducky': (181, 240)}

while time and tasks:

    result = time[0] * tasks[-1]
    for duck_type, needed_time in ducky_type.items():

        if result in range(needed_time[0], needed_time[1] + 1):
            rubber_ducks_info[duck_type] += 1
            time.popleft()
            tasks.pop()
            break
    else:
        tasks[-1] -= 2
        time.rotate(-1)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print('\n'.join(f'{k}: {v}' for k, v in rubber_ducks_info.items()))
