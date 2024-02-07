clothes_sequence = [int(x) for x in input().split()]
rack_capacity = int(input())
counter = 0
summary = 0

while clothes_sequence:
    summary += clothes_sequence[-1]
    if summary == rack_capacity:
        clothes_sequence.pop()
        if clothes_sequence:
            counter += 1
            summary = 0
    elif summary > rack_capacity:
        counter += 1
        summary = 0
        summary += clothes_sequence.pop()
    else:
        clothes_sequence.pop()
    if summary > 0 and len(clothes_sequence) == 0:
        counter += 1

print(counter)
