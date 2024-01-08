numbers = tuple(map(float,input().split()))

number_count = {}
for num in numbers:
    if num not in number_count:
        number_count[num] = numbers.count(num)
    else:
        continue

for k, v in number_count.items():
    print(f'{k} - {v} times')
    