import os

path = os.path.join("text_doc", 'numbers.txt')
file = open(path)

total = 0
for line in file.readlines():
    total += int(line.strip())

print(total)