matrix = [[i.strip() for i in el.split()]for el in input().split('|')]
flatten_list = []

while matrix:
    current_list = matrix.pop()
    flatten_list.extend(current_list)
print(*flatten_list)
