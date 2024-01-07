from collections import deque


def format_time(h: int, m: int, s: int):
    if s > 59:
        s %= 60
        m += 1
    if m > 59:
        m %= 60
        h += 1
    if h > 23:
        h = 0
    return h, m, s


user_input = input().split(';')
time = input().split(':')

hour = int(time[0])
minutes = int(time[1])
seconds = int(time[2])

robots = {}
process_time = {}
products = deque()

for i in user_input:
    result = i.split('-')
    robots[result[0]] = int(result[1])

command = input()
while command != 'End':
    products.append(command)
    command = input()

while products:
    seconds += 1
    hour, minutes, seconds = format_time(hour, minutes, seconds)
    length_process_time = process_time.copy()

    for robot in length_process_time:
        process_time[robot] -= 1
        if process_time[robot] == 0:
            del process_time[robot]

    for robot, time in robots.items():
        if robot not in process_time:
            print(f'{robot} - {products.popleft()} [{hour:02d}:{minutes:02d}:{seconds:02d}]')
            process_time[robot] = time
            break
    else:
        products.rotate(-1)

