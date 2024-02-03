import os

command = input().split('-')

while command[0] != 'End':

    file_name = command[1]
    path = os.path.join('text_folder', file_name)

    if command[0] == 'Create':
        file = open(path, 'w')
        file.close()
    elif command[0] == 'Add':
        content = command[2]

        with open(path, 'a') as file:
            file.write(f"{content}\n")

    elif command[0] == 'Replace':
        old_string = command[2]
        new_string = command[3]
        try:
            with open(path, 'r+') as file:
                text = file.read()
                text = text.replace(old_string, new_string)
                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == 'Delete':
        try:
            os.remove(path)
        except FileNotFoundError:
            print('An error occurred')

    command = input().split('-')
