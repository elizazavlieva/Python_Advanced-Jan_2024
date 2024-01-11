import operator
from collections import deque

working_bees = deque(map(int, input().split()))
nectar = [int(i) for i in input().split()]
symbols = deque(input().split())

operation = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv
             }

total_honey = 0
while working_bees and nectar:
    if working_bees[0] > nectar[-1]:
        nectar.pop()
    else:
        symbol = symbols.popleft()
        if symbol == '/' and nectar[-1] == 0:
            working_bees.popleft()
            nectar.pop()
        else:
            total_honey += abs(operation[symbol](working_bees.popleft(), nectar.pop()))

print(f'Total honey made: {total_honey}')
if working_bees:
    print(f'Bees left: {", ".join([str(i) for i in working_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(i) for i in nectar])}')
