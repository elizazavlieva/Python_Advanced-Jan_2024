from collections import deque

def math_operations(*args, **kwargs):
    numbers = deque([el for el in args])

    while numbers:
        for key, value in kwargs.items():
            if len(numbers) == 0:
                break
            num = numbers.popleft()
            if key == 'a':
                kwargs[key] += num
            elif key == 's':
                kwargs[key] -= num
            elif key == 'd':
                if num != 0:
                    kwargs[key] /= num
            elif key == 'm':
                kwargs[key] *= num

    sorted_elements = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    return '\n'.join([f'{el[0]}: {el[1]:.1f}' for el in sorted_elements])


'''TESTS'''
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))