stack = []


for i in range(int(input())):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif stack:
        if command[0] == '2':
            stack.pop()
        elif command[0] == '3':
            print(max(stack))
        elif command[0] == '4':
            min_value = min(stack)
            print(min_value)

stack.reverse()

print(*stack, sep=', ')
