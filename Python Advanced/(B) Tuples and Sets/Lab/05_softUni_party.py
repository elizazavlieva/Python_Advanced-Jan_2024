n = int(input())
guests_list = set(input() for _ in range(n))

command = input()
while command != 'END':
    if command in guests_list:
        guests_list.remove(command)
    command = input()

print(f'{len(guests_list)}')
for guest in sorted(guests_list):
    print(guest)
