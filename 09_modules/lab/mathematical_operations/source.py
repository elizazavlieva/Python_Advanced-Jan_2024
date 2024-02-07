from math import floor


def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Zero can\'t be divider"


def power(num1, num2):
    return truncate(pow(num1, num2), 2)


operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              '^': power}


def math_operation(equation):
    operator = equation[1]
    first_num = float(equation[0])
    second_num = int(equation[2])

    return operations[operator](first_num, second_num)