def shopping_cart(*args):
    shopping_list = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for command in args:
        if command == 'Stop':
            break
        food = command[0]
        product = command[1]
        if food == 'Pizza' and len(shopping_list[food]) == 4:
            continue
        elif food == 'Soup' and len(shopping_list[food]) == 3:
            continue
        elif food == 'Dessert' and len(shopping_list[food]) == 2:
            continue

        if product not in shopping_list[food]:
            shopping_list[food].append(product)

    for elements in shopping_list.values():
        if elements:
            break
    else:
        return 'No products in the cart!'

    sorted_list = sorted(shopping_list.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for food, products in sorted_list:
        result += f'{food}:\n'
        for el in sorted(products):
            result += f' - {el}\n'
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
