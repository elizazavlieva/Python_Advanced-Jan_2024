from collections import deque

food_supply = [int(el) for el in input().split(', ')]
stamina = deque(int(el) for el in input().split(', '))

peaks = deque([(80, 'Vihren'), (90, 'Kutelo'), (100, 'Banski Suhodol'),
               (60, 'Polezhan'), (70, 'Kamenitza')])


day = 1
conquered_peaks = []
while peaks and food_supply and stamina and day < 8:
    result = food_supply.pop() + stamina.popleft()
    if result >= peaks[0][0]:
        conquered_peaks.append(peaks[0][1])
        peaks.popleft()
        day += 1
    else:
        day += 1


if peaks:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if conquered_peaks:
    print('Conquered peaks:')
    [print(el) for el in conquered_peaks]
