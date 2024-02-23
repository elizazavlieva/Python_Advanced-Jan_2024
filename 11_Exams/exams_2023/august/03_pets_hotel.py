def accommodate_new_pets(capacity, max_weight, *args):
    pet_data = {}
    result = []

    for pet_type, weight in args:
        if capacity <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if weight > max_weight:
            continue
        if pet_type not in pet_data:
            pet_data[pet_type] = 0
        pet_data[pet_type] += 1
        capacity -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {capacity}.')

    result.append('Accommodated pets:')
    [result.append(f'{pet}: {number}') for pet, number in sorted(pet_data.items())]
    return '\n'.join(result)


'''TESTS'''

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
