"""
You have an empty stack. You will receive an integer – N. On the following N lines,
you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
"""

stack = []
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif stack:
        if command[0] == '2':
            stack.pop()
        elif command[0] == '3':
            print(max(stack))
        elif command[0] == '4':
            min_value = min(stack)
            print(min_value)

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
