from collections import deque

seats = input().split(', ')
first_line = deque(int(el) for el in input().split(', '))
second_line = deque(int(el) for el in input().split(', '))

rotations = 0
taken_seats = []

while len(taken_seats) != 3 and rotations != 10:
    first_num = first_line[0]
    second_num = second_line[-1]
    letter = chr(first_num + second_num)
    first_seat = str(first_num) + letter
    second_seat = str(second_num) + letter

    if first_seat in seats or second_seat in seats:

        if first_seat in seats and first_seat not in taken_seats:
            taken_seats.append(first_seat)
        elif second_seat in seats and second_seat not in taken_seats:
            taken_seats.append(second_seat)

        first_line.popleft()
        second_line.pop()

    else:
        first_line.rotate(-1)
        second_line.rotate(1)
        
    rotations += 1


print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
