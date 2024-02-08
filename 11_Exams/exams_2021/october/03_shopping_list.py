def shopping_list(budget, **kwargs):
    products = set()
    result = []

    if budget < 100:
        return 'You do not have enough budget.'

    for item, (price, qnty) in kwargs.items():
        if len(products) == 5:
            break

        total_price = price * qnty
        if total_price <= budget:
            result.append(f'You bought {item} for {total_price:.2f} leva.')
            products.add(item)
            budget -= total_price
        else:
            continue

    return "\n".join(result)


'''TESTS'''
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
