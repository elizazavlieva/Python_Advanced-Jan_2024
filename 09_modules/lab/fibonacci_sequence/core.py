def create_sequence(n):
    fibonacci = [0, 1]

    for _ in range(n - 2):
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
    return fibonacci


def locate_number(number, fibonacci):
    try:
        return f'The number - {number} is at index {fibonacci.index(number)}'
    except ValueError:
        return f"The number {number} is not in the sequence"
