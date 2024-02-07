import pyfiglet


def figlet_format(text):
    return pyfiglet.figlet_format(text)


line = input()
print(figlet_format(line))