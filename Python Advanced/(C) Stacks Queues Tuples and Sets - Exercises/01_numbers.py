first_sequence = set([int(i) for i in input().split()])
second_sequence = set([int(i) for i in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    numbers = set([int(i) for i in command if i.isdigit()])
    if command[0] == 'Add':
        if command[1] == 'First':
            first_sequence = first_sequence.union(numbers)
        else:
            second_sequence = second_sequence.union(numbers)
    elif command[0] == 'Remove':
        if command[1] == 'First':
            first_sequence = first_sequence.difference(numbers)
        else:
            second_sequence = second_sequence.difference(numbers)
    if command[0] == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print('True')
        else:
            print('False')
print(', '.join([str(i) for i in sorted(first_sequence)]))
print(', '.join([str(i) for i in sorted(second_sequence)]))
