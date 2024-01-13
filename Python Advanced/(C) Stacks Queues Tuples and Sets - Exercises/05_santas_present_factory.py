from collections import deque

materials = [int(i) for i in input().split()]
magic = deque(map(int, input().split()))
present_value = {
                'Doll': 150,
                'Wooden train': 250,
                'Teddy bear': 300,
                'Bicycle': 400
}
completed_presents = dict()
while materials and magic:
    if magic[0] == 0 or materials[-1] == 0:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()
    else:
        result = materials[-1] * magic[0]
        if result < 0:
            materials.append(materials.pop() + magic.popleft())
        elif result in present_value.values():
            for k, v in present_value.items():
                if v == result:
                    if k not in completed_presents:
                        completed_presents[k] = 1
                    else:
                        completed_presents[k] += 1
                    break
            materials.pop()
            magic.popleft()
        else:
            magic.popleft()
            materials[-1] += 15

if ('Doll' in completed_presents and 'Wooden train' in completed_presents) or ('Teddy bear' in completed_presents
                                                                               and 'Bicycle' in completed_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(str(i) for i in materials[::-1])}')

if magic:
    print(f'Magic left: {", ".join(str(i) for i in magic)}')

completed_presents = dict(sorted(completed_presents.items()))

for k, v in completed_presents.items():
    print(f'{k}: {v}')
