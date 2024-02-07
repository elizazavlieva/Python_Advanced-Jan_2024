import os
import string

path = os.path.join("text_folder", 'text.txt')

with open(path) as file:
    text = file.readlines()

path = os.path.join("text_folder", "output.txt")
for i in range(len(text)):
    punctuation_count, letters_count = 0, 0

    for char in text[i]:
        if char in string.punctuation:
            punctuation_count += 1
        elif char.isalpha():
            letters_count += 1

    line = text[i].replace('\n', '')

    with open(path, 'a') as file:
        file.write(f"Line {i + 1}: {line} ({letters_count})({punctuation_count})\n")