def even_odd(*args):
    numbers = []
    command = ''
    for el in args:
        if isinstance(el, int):
            numbers.append(el)
        else:
            command = el

    if command == 'even':
        return [i for i in numbers if i % 2 == 0]
    elif command == 'odd':
        return [i for i in numbers if i % 2 != 0]



'''TESTS'''
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
