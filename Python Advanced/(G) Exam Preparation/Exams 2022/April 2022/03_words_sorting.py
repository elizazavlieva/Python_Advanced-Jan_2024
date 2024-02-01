def words_sorting(*args):
    word_info = {}
    for word in args:
        if word not in word_info:
            word_info[word] = 0
        word_info[word] = sum([ord(el) for el in word])
    if sum(word_info.values()) % 2 == 0:
        sorted_words = sorted(word_info.items())
    else:
        sorted_words = sorted(word_info.items(), key=lambda kvp: (-kvp[1]))

    return "\n".join([f'{key} - {value}' for key, value in sorted_words])




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
