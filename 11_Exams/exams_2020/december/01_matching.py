from collections import deque

males = [int(el) for el in input().split()]
females = deque(int(el) for el in input().split())
matches = 0
while females and males:

    male = males[-1]
    female = females[0]
    if male <= 0:
        males.pop()
        continue
    if female <= 0:
        females.popleft()
        continue
    if male % 25 == 0:
        for _ in range(2):
            if males:
                males.pop()
        continue
    if female % 25 == 0:
        for _ in range(2):
            if females:
                females.popleft()
        continue

    if male == female:
        matches += 1
        males.pop()
        females.popleft()

    else:
        males[-1] -= 2
        females.popleft()

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(str(el) for el in males[::-1])}')
else:
    print('Males left: none')
if females:
    print(f'Females left: {", ".join(str(el) for el in females)}')
else:
    print('Females left: none')
