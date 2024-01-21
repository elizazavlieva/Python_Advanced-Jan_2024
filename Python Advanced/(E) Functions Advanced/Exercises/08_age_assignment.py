def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for key, value in kwargs.items():
            if name.startswith(key):
                result[name] = value
    sorted_names = sorted(result.items(), key=lambda kvp: kvp[0])
    return '\n'.join([f"{elem[0]} is {elem[1]} years old." for elem in sorted_names])


'''TESTS'''
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))