from collections import deque

vowels = deque(map(str, input().split()))
consonants = list(map(str, input().split()))

flowers_info = {'rose': {}, 'tulip': {}, 'lotus': {}, 'daffodil': {}}
found_word = ''
is_found = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower, info in flowers_info.items():
        if vowel in flower:
            counter = flower.count(vowel)

            if vowel not in flowers_info[flower]:
                flowers_info[flower][vowel] = counter

        if consonant in flower:
            counter = flower.count(consonant)

            if consonant not in flowers_info[flower]:
                flowers_info[flower][consonant] = counter

        if sum(flowers_info[flower].values()) == len(flower):
            found_word = flower
            is_found = True
            break

    if is_found:
        print(f"Word found: {found_word}")
        break

if not is_found:
    print("Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')