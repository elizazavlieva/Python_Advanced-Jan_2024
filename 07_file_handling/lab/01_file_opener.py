import os

path = os.path.join("text_doc", "text.txt")

try:
    file = open(path)
    print('File found')

except FileNotFoundError:

    print('File not found')
