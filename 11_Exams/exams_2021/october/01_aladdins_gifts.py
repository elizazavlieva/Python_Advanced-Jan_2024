from collections import deque


def checking_ranges(magic_level_data, result):
    for present, ranges in magic_level_data.items():
        if result in range(ranges[0], ranges[1]):
            return present


def below_range(magic_level_data, result, material, magic_level):
        if result % 2 == 0:
            result = (magic_level * 3) + (material * 2)
            return checking_ranges(magic_level_data, result)
        else:
            result *= 2
            return checking_ranges(magic_level_data, result)


def above_range(magic_level_data, result):
        result /= 2
        return checking_ranges(magic_level_data, int(result))


def adding_crafted_present(crafted_presents, crafting_proces):
    if crafting_proces not in crafted_presents:
        crafted_presents[crafting_proces] = 0
    crafted_presents[crafting_proces] += 1
    return crafted_presents


def is_task_completed(presents, needed_pairs):
    for pairs in needed_pairs:
        if pairs[0] in presents and pairs[1] in presents:
            return True

    return False


materials = list(map(int, input().split()))
magic_level_value = deque(map(int, input().split()))
magic_level_data = {'Gemstone': (100, 200),
                    'Porcelain Sculpture': (200, 300),
                    'Gold': (300, 400),
                    'Diamond Jewellery': (400, 500)}

needed_pairs = [["Gemstone", "Porcelain Sculpture"], ["Gold", "Diamond Jewellery"]]
crafted_presents = {}


is_completed = False

while magic_level_value and materials:
    material = materials.pop()
    magic_level = magic_level_value.popleft()

    result = material + magic_level
    crafting_proces = checking_ranges(magic_level_data, result)

    if crafting_proces:
        crafted_presents = adding_crafted_present(crafted_presents, crafting_proces)

    else:
        if result < 100:
            crafting_proces = below_range(magic_level_data, result, material, magic_level)
        if result > 499:
            crafting_proces = above_range(magic_level_data, result)

        if crafting_proces:
            crafted_presents = adding_crafted_present(crafted_presents, crafting_proces)

    is_completed = is_task_completed(crafted_presents, needed_pairs)

if is_completed:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_level_value:
    print(f'Magic left: {", ".join(map(str, magic_level_value))}')

[print(f"{present}: {count}") for present, count in sorted(crafted_presents.items(), key=lambda kvp: kvp[0])]