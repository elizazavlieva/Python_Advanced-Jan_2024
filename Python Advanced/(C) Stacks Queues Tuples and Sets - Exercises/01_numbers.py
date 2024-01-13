first_line = set([int(i) for i in input().split()])
second_line = set([int(i) for i in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    numbers = set([int(i) for i in command if i.isdigit()])
    if command[0] == 'Add':
        if command[1] == 'First':
            first_line = first_line | numbers
        else:
            second_line = second_line | numbers
    elif command[0] == 'Remove':
        if command[1] == 'First':
            first_line = first_line - numbers
        else:
            second_line = second_line - numbers
    if command[0] == 'Check':
        if first_line < second_line or second_line < first_line:
            print('True')
        else:
            print('False')
print(', '.join([str(i) for i in sorted(first_line)]))
print(', '.join([str(i) for i in sorted(second_line)]))
