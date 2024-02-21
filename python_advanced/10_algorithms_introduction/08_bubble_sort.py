def buble_sort(numbers):
    count = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(1, len(numbers) - count):
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
                is_sorted = False
        count += 1
    return numbers


numbers = [int(el) for el in input().split()]

print(*buble_sort(numbers), sep=" ")
