n = int(input())
parking_info = set()

for _ in range(n):
    car = input().split(", ")
    if car[0] == 'IN':
        parking_info.add(car[1])
    elif car[0] == 'OUT':
        if car[1] in parking_info:
            parking_info.remove(car[1])

if parking_info:
    for i in parking_info:
        print(i)
else:
    print('Parking Lot is Empty')
