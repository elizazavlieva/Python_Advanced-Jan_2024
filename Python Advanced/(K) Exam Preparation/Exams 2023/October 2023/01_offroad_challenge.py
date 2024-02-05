from collections import deque

initial_fuel = [int(el) for el in input().split()]
consumption_index = deque(int(el) for el in input().split())
fuel_needed = deque(int(el) for el in input().split())

altitudes = []
counter = 0

while initial_fuel and consumption_index and fuel_needed:

    result = initial_fuel[-1] - consumption_index[0]
    counter += 1

    if result >= fuel_needed[0]:

        initial_fuel.pop()
        consumption_index.popleft()
        fuel_needed.popleft()

        altitudes.append(f'Altitude {counter}')
        print(f'John has reached: Altitude {counter}')
    else:

        initial_fuel.pop()
        consumption_index.popleft()
        fuel_needed.popleft()
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

