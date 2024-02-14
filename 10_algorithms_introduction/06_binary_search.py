def binary_search(numbers, num):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid_index = (left + right) // 2
        if numbers[mid_index] == num:
            return mid_index
        elif numbers[mid_index] < num:
            left = mid_index + 1
        elif numbers[mid_index] > num:
            right = mid_index - 1
    return -1


numbers = [int(el) for el in input().split()]
num = int(input())

print(binary_search(numbers, num))