import os.path
import re

word_path = os.path.join('text_doc', 'words.txt')
text = os.path.join('text_doc', 'text.txt')
word_text = os.path.join('text_doc', 'output.txt')

with open(word_path) as file:
    searched_words = file.read().lower().split()

with open(text) as file:
    content = file.read().lower()

words_info = {}

for word in searched_words:
    pattern = re.compile(rf"\b{word}\b")
    result = re.findall(pattern, content)
    words_info[word] = result.count(word)

sorted_info = sorted(words_info.items(), key=lambda kvp: (-kvp[1]))

with open(word_text, 'a') as file:
    for word, count in sorted_info:
        file.write(f"{word} - {count}\n")