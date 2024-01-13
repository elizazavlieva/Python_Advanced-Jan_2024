n = int(input())
first_line = set()
second_line = set()
longest_line = set()

for _ in range(n):
    user_input = input().split('-')
    first_start, first_end = user_input[0].split(',')
    second_start, second_end = user_input[1].split(',')
    first_line = {num for num in range(int(first_start), int(first_end) + 1)}
    second_line = {num for num in range(int(second_start), int(second_end) + 1)}
    current_line = first_line.intersection(second_line)
    if len(current_line) > len(longest_line):
        longest_line = current_line
    first_line.clear()
    second_line.clear()

print(f"Longest intersection is {list(map(lambda x: x, longest_line))} with length {len(longest_line)}")
