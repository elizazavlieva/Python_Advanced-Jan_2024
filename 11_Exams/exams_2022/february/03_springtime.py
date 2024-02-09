def start_spring(**kwargs):
    spring_items = {}

    for name, type_ in kwargs.items():
        if type_ not in spring_items:
            spring_items[type_] = []

        spring_items[type_].append(name)

    sorted_item = sorted(spring_items.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = []
    for object_type, items in sorted_item:
        result.append(f'{object_type}:')
        [result.append(f'-{item}') for item in sorted(items)]

    return "\n".join(result)


'''TESTS'''

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
