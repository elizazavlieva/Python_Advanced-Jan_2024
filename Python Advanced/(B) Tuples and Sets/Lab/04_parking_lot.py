n = int(input())
parking_info = set()

for _ in range(n):
    car = input().split(", ")
    if car[0] == 'IN':
        parking_info.add(car[1])
    else:
        parking_info.remove(car[1])

if parking_info:
    for i in parking_info:
        print(i)
else:
    print('Parking Lot is Empty')
