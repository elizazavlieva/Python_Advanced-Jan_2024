from collections import deque

textiles = deque(int(el) for el in input().split())
medicament = [int(el) for el in input().split()]

items = {'Patch': 30,'Bandage': 40,'MedKit': 100}
created_items = {}

while textiles and medicament:
    result = textiles[0] + medicament[-1]
    for item, resource in items.items():
        if resource == result:
            if item not in created_items:
                created_items[item] = 0
            created_items[item] += 1
            textiles.popleft()
            medicament.pop()
            break
    else:
        last_key = list(items)[-1]
        if items[last_key] < result:
            if last_key not in created_items:
                created_items[last_key] = 0
            created_items[last_key] += 1
            diff = result - items[last_key]
            textiles.popleft()
            medicament.pop()
            medicament[-1] += diff
        else:
            medicament[-1] += 10
            textiles.popleft()

sorted_items = sorted(created_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
if not medicament and not textiles:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicament:
    print("Medicaments are empty.")


if sorted_items:
    [print(f'{key} - {value}') for key, value in sorted_items]

medicament.reverse()

if medicament:
    print(f'Medicaments left: {", ".join(str(el) for el in medicament)}')
if textiles:
    print(f'Textiles left: {", ".join(str(el) for el in textiles)}')


