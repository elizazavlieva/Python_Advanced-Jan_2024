from core import create_sequence, locate_number

command = input()
sequence = []
while command != 'Stop':
    if "Create" in command:
        _, _, num = command.split()
        sequence = create_sequence(int(num))
        print(*sequence)
    else:
        _, num = command.split()
        result = locate_number(int(num), sequence)
        print(result)
    command = input()

