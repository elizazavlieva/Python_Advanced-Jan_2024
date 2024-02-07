import os

path = os.path.join("text_folder", 'text.txt')

with open(path) as file:
    text = file.readlines()

symbols = ["-", ",", ".", "!", "?"]

for i in range(len(text)):
    if i % 2 == 0:
        for el in symbols:
            text[i] = text[i].replace(el, '@')
        line = text[i].split()
        print(" ".join(line[::-1]))


