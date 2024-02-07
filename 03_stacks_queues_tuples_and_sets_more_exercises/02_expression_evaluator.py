import math
from collections import deque

string_expression = deque(input().split())
index = len(string_expression)
numbers = deque()
result = 0

while string_expression:
    if index == len(string_expression) and string_expression[0].isdigit():
        result = string_expression.popleft()
    else:
        symbol = string_expression.popleft()
        if symbol.isdigit() or len(symbol) > 1:
            numbers.append(symbol)
        else:
            while numbers:
                result = eval(str(result) + symbol + numbers.popleft())
            result = math.floor(result)

print(result)
