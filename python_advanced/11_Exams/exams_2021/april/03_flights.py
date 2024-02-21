from collections import deque


def flights(*args):
    flights_info = deque(args)
    flights_collection = {}

    while flights_info:
        flight = flights_info.popleft()

        if flight == 'Finish':
            break

        passengers = int(flights_info.popleft())
        if flight not in flights_collection:
            flights_collection[flight] = 0

        flights_collection[flight] += passengers

    return flights_collection


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))