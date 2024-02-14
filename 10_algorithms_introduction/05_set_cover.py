def set_cover(universe, sets):
    chosen_sets = []
    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        chosen_sets.append(best_set)
        universe -= best_set
    return chosen_sets


universe = {int(el) for el in input().split(", ")}
sets_count = int(input())
sets = [set(int(el) for el in input().split(", ")) for _ in range(sets_count)]

result = set_cover(universe, sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")
[print('{ ' + f'{", ".join(map(str, s))}' + ' }') for s in result]