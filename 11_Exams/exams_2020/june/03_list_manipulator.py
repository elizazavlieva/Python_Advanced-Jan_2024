def list_manipulator(num_list, command, position, *args):
    parameters = []
    if args:
        parameters = [int(el) for el in args]

    if command == 'add':
        if position == 'end':
            if parameters:
                num_list.extend(parameters)
            return list(num_list)

        elif position == 'beginning':
            if parameters:
                parameters.extend(num_list)
            return list(parameters)

    elif command == 'remove':
        if position == 'end':
            if parameters:
                for _ in range(parameters[0]):
                    num_list.pop()
            else:
                num_list.pop()

            return list(num_list)

        elif position == 'beginning':
            if parameters:
                counter = 0
                while counter < parameters[0]:
                    num_list.pop(0)
                    counter += 1
            else:
                num_list.pop(0)

            return list(num_list)


'''TESTS'''
print(list_manipulator([1,2,3], "remove", "end"))                   
print(list_manipulator([1,2,3], "remove", "beginning"))             
print(list_manipulator([1,2,3], "add", "beginning", 20))            
print(list_manipulator([1,2,3], "add", "end", 30))                  
print(list_manipulator([1,2,3], "remove", "end", 2))                
print(list_manipulator([1,2,3], "remove", "beginning", 2))          
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))          
