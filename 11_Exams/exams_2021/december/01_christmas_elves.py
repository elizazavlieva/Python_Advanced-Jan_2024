from collections import deque

elf_energy = deque(map(int, input().split()))
materials_box = list(map(int, input().split()))

total = {"Toys": 0, "Energy": 0}


def make_presents(material, total, toys=0):
    for commands, value in total.items():
        if commands == "Energy":
            total[commands] += material
        elif commands == "Toys":
            total[commands] += toys
    return total


def multipy(material):
    return material * 2


def checking_energy(elf, material):
    if elf >= material:
        return True
    return False


def every_fifth_time( material, total, command):
    total[command] += material
    return total


def not_enough_energy(elf, material, elf_energy, materials_box):
    elf_energy.append(elf * 2)
    materials_box.append(material)
    return elf_energy, materials_box


def calculation(counter, elf, material):
    if counter % 5 == 0:
        return elf - material
    return elf - (material - 1)


counter = 0
while elf_energy and materials_box:
    elf = elf_energy.popleft()
    if elf < 5:
        continue

    counter += 1
    material = materials_box.pop()

    if counter % 5 == 0:
        if counter % 3 == 0 and checking_energy(elf, multipy(material)):
            total = every_fifth_time(multipy(material), total, "Energy")
            elf_energy.append(calculation(counter, elf, multipy(material)))

        elif counter % 3 != 0 and checking_energy(elf, material):
            total = make_presents(material, total)
            elf_energy.append(calculation(counter, elf, material))

        else:
            elf_energy, materials_box = not_enough_energy(elf, material, elf_energy, materials_box)

    elif counter % 3 == 0:
        if checking_energy(elf, multipy(material)):

            total = make_presents(multipy(material), total, 2)
            elf_energy.append(calculation(counter, elf, multipy(material)))

        else:
            elf_energy, materials_box = not_enough_energy(elf, material, elf_energy, materials_box)

    else:
        if checking_energy(elf, material):
            total = make_presents(material, total, 1)
            elf_energy.append(calculation(counter, elf, material))

        else:
            elf_energy, materials_box = not_enough_energy(elf, material, elf_energy, materials_box)

for items, count in total.items():
    print(f"{items}: {count}")

if elf_energy:
    print(f"Elves left: {', '.join(map(str, elf_energy))}")
if materials_box:
    print(f"Boxes left: {', '.join(map(str, materials_box))}")