def naughty_or_nice_list(kids_list, *commands, **keyword_commands):
    santa_data = {"Nice": [],
                  "Naughty": [],
                  'Not found': []}

    for el in commands:
        num, type_ = [int(i) if i.isdigit() else i for i in el.split("-")]
        kids_count = [kid for kid in kids_list if kid[0] == num]

        if len(kids_count) == 1:
            santa_data[type_].append(kids_count[0][1])
            kids_list.remove(kids_count[0])

    for name, category in keyword_commands.items():
        kids_count = [kid for kid in kids_list if kid[1] == name]

        if len(kids_count) == 1:
            santa_data[category].append(kids_count[0][1])
            kids_list.remove(kids_count[0])

    santa_data['Not found'] = [kid for _, kid in kids_list]

    return "\n".join([f"{type_}: {', '.join(info)}" for type_, info in santa_data.items() if info])


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
