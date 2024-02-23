def operations(num):
    negative_num = []
    positive_num = []
    for i in num:
        if i < 0:
            negative_num.append(i)
        else:
            positive_num.append(i)

    def negative_sum():
        return sum(negative_num)

    def positive_sum():
        return sum(positive_num)

    def larger_sum():
        if abs(sum(negative_num)) > sum(positive_num):
            return 'The negatives are stronger than the positives'
        else:
            return 'The positives are stronger than the negatives'

    result = f'{negative_sum()}\n{positive_sum()}\n{larger_sum()}'
    return result


number = [int(el) for el in input().split()]
print(operations(number))
