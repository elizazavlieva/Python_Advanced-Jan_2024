from collections import deque

substrings = deque(input().split())
main_colors = []
all_colors = []
main_color_info = ['red', 'yellow', 'blue']
secondary_color_info = {'orange': ['red', 'yellow'],
                        'purple': ['red', 'blue'],
                        'green': ['yellow', 'blue']}

while substrings:

    if len(substrings) > 1:
        first = substrings.popleft()
        last = substrings.pop()
    else:
        first = substrings.popleft()
        last = ''

    first_option = first + last
    second_option = last + first

    if first_option in main_color_info:
        main_colors.append(first_option)
        all_colors.append(first_option)
    elif second_option in main_color_info:
        main_colors.append(second_option)
        all_colors.append(second_option)
    elif first_option in secondary_color_info.keys():
        all_colors.append(first_option)
    elif second_option in secondary_color_info.keys():
        all_colors.append(second_option)
    else:
        first = first[0:-1]
        last = last[0:-1]
        if first:
            substrings.insert(len(substrings) // 2, first)
        if last:
            substrings.insert(len(substrings) // 2, last)

result = []
for index in range(len(all_colors)):
    if all_colors[index] in main_colors:
        result.append(all_colors[index])
    else:
        for k, v in secondary_color_info.items():
            if all_colors[index] == k:
                is_valid = all(i in main_colors for i in v)
                if is_valid:
                    result.append(all_colors[index])
print(result)
