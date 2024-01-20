from functools import reduce


def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = reduce(lambda x, y: x - y, args)
        return result

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        result = reduce(lambda x, y: x / y, args)
        return result
    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
