n = int(input())

odd_set = set()
even_set = set()
summary = 0
for i in range(1, n + 1):
    names = [ord(i) for i in input()]
    summary = sum(names) // i
    if summary % 2 == 0:
        even_set.add(summary)
    else:
        odd_set.add(summary)

if sum(even_set) == sum(odd_set):
    print(", ".join([str(num) for num in odd_set | even_set]))

elif sum(odd_set) > sum(even_set):
    print(", ".join([str(num) for num in odd_set - even_set]))

elif sum(even_set) > sum(odd_set):
    print(", ".join([str(num) for num in odd_set ^ even_set]))
