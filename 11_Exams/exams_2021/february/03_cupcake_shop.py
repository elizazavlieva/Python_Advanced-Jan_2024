from collections import deque


def stock_availability(boxes, command, *args):
    cupcake_boxes = deque(boxes)
    if command == 'delivery':
        cupcake_boxes.extend(args)

    elif command == 'sell':

        if args:
            for item in args:
                if isinstance(item, str) and item in cupcake_boxes:
                    cupcake_boxes = [el for el in cupcake_boxes if el != item]

                elif isinstance(item, int):
                    [cupcake_boxes.popleft() for _ in range(item)]

        else:
            cupcake_boxes.popleft()

    return list(cupcake_boxes)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
