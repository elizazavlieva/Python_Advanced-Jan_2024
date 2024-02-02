import os

path = os.path.join('text_doc', 'my_first_file.txt')

try:
    os.remove(path)
except FileNotFoundError:
    print('File is already deleted!')


# second solution

if os.path.exists(path):
    os.remove(path)
else:
    print('File is already deleted!')