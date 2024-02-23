def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if key == 'odd':
            result[key] = [el for el in value if el % 2 != 0]
        elif key == 'even':
            result[key] = [el for el in value if el % 2 == 0]
    return dict(sorted(result.items(), key=lambda kvp: -len(kvp[1])))


'''TESTS'''
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
