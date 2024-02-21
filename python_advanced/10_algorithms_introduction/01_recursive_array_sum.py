def summary(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + summary(numbers, index + 1)


nums = list(map(int, input().split()))

print(summary(nums))
