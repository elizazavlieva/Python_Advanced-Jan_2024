def even_odd(*args):
    result = []
    numbers = []
    command = ''
    for el in args:
        if isinstance(el, int):
            numbers.append(el)
        else:
            command = el

    def even():
        return [i for i in numbers if i % 2 == 0]

    def odd():
        return [i for i in numbers if i % 2 != 0]
    if command == 'even':
        result = even()
    elif command == 'odd':
        result = odd()
    return result


'''TESTS'''
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
