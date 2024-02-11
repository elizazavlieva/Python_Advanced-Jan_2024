import os

path = os.path.join("text_folder", 'text.txt')

with open(path) as file:
    text = file.readlines()

symbols = ["-", ",", ".", "!", "?"]

for i in range(0, len(text), 2):
    for el in symbols:
        text[i] = text[i].replace(el, '@')
    print(" ".join(text[i].split()[::-1]))


