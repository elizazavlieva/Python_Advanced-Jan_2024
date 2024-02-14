def selection_sort(numbers):
    for index in range(len(numbers)):
        min_index = index
        for cur_index in range(index + 1, len(numbers)):
            if numbers[cur_index] < numbers[min_index]:
                min_index = cur_index
        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]


numbers = [int(el) for el in input().split()]
selection_sort(numbers)
print(*numbers)