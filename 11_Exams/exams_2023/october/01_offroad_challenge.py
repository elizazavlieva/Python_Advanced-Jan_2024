from collections import deque


def removing_values(initial_fuel, consumption_index, fuel_needed):
    initial_fuel.pop()
    consumption_index.popleft()
    fuel_needed.popleft()
    return initial_fuel, consumption_index, fuel_needed


initial_fuel = [int(el) for el in input().split()]
consumption_index = deque(int(el) for el in input().split())
fuel_needed = deque(int(el) for el in input().split())

altitudes = []
counter = 0


while initial_fuel and consumption_index and fuel_needed:

    result = initial_fuel[-1] - consumption_index[0]
    counter += 1

    if result >= fuel_needed[0]:
        removing_values(initial_fuel, consumption_index, fuel_needed)
        altitudes.append(f'Altitude {counter}')
        print(f'John has reached: Altitude {counter}')
    else:
        removing_values(initial_fuel, consumption_index, fuel_needed)
        print(f'John did not reach: Altitude {counter}')
        break

if len(altitudes) == 4:
    print('John has reached all the altitudes and managed to reach the top!')
else:
    print('John failed to reach the top.')

    if altitudes:
        print(f'Reached altitudes: {", ".join(altitudes)}')
    else:
        print('John didn\'t reach any altitude.')

