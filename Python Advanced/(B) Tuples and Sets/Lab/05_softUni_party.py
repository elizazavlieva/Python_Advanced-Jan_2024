n = int(input())
guests_list = set()
for _ in range(n):
    guest = input()
    guests_list.add(guest)

command = input()
while command != 'END':
    if command in guests_list:
        guests_list.remove(command)
    command = input()

vip_guest = sorted([i for i in guests_list if i[0].isdigit()])
regular_guest = sorted([i for i in guests_list if i[0].isalpha()])
print(f'{len(vip_guest) + len(regular_guest)}')
for guest in vip_guest:
    print(guest)
for guest in regular_guest:
    print(guest)
