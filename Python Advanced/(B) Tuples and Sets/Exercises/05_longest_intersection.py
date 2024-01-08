n = int(input())
intersection_one = set()
intersection_two = set()
longest_intersection = set()

for _ in range(n):
    user_input = input().split('-')
    first_start, first_end = user_input[0].split(',')
    second_start, second_end = user_input[1].split(',')
    for num in range(int(first_start), int(first_end) + 1):
        intersection_one.add(num)
    for num in range(int(second_start), int(second_end) + 1):
        intersection_two.add(num)
    current_intersection = intersection_one.intersection(intersection_two)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = intersection_one.intersection(intersection_two)
    intersection_one.clear()
    intersection_two.clear()

item_list = list(map(lambda x: x, longest_intersection))

print(f"Longest intersection is {item_list} with length {len(item_list)}")