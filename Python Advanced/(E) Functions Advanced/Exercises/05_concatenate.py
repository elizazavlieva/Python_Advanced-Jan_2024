def concatenate(*args, **kwargs):
    result = ''.join(args)

    for old_str, new_str in kwargs.items():
        result = result.replace(old_str, new_str)
    return result


'''TESTS'''
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))