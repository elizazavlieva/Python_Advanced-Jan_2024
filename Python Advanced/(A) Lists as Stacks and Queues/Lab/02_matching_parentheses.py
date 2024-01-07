"""
Scanning through algebraic expression
and extract each set of parentheses using stacks.
user input:
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
(2 + 3) - (2 + 3)
"""

text = input()
stack = []

for i in range(len(text)):
    if text[i] == '(':
        stack.append(i)
    if text[i] == ')':
        index = stack.pop()
        print(text[index:i+1])
