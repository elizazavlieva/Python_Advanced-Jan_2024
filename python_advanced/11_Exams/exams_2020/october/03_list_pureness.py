import sys
from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    pureness_value = -sys.maxsize
    count_rotation = 0

    for counter in range(k + 1):
        current_value = 0

        for index in range(len(numbers)):
            current_value += (numbers[index] * index)

        if current_value > pureness_value:
            pureness_value = current_value
            count_rotation = counter
        numbers.rotate(1)

    return f'Best pureness {pureness_value} after {count_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
