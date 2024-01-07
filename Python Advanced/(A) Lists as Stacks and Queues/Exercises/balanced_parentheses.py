from collections import deque

symbol = deque(input())
counter = 0
rotation = len(symbol) * 2
while symbol and counter < rotation:
    for i in range(len(symbol)):
        if (symbol[i] == '(' and symbol[i + 1] == ')') or (symbol[i] == '{' and symbol[i + 1] == '}') or \
                (symbol[i] == '[' and symbol[i + 1] == ']'):
            symbol.popleft()
            symbol.popleft()
            counter = 0
            break
        else:
            symbol.rotate(-1)
            counter += 1
            break

if symbol:
    print("NO")
else:
    print('YES')
    