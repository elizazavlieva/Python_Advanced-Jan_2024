def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    free_cubes = 0
    for num in args:
        if num == 'Finish':
            break
        if box_size - num <= 0:
            num -= box_size
            box_size = 0
        if box_size > 0:
            box_size -= num
        else:
            free_cubes += num


    if box_size <= 0:
        return f'No more free space! You have {free_cubes} more cubes.'
    else:
        return f'There is free space in the box. You could put {box_size} more cubes.'


'''TESTS'''
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
