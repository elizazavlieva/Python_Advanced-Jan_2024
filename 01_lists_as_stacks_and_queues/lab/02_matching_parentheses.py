text = input()
stack = []

for i in range(len(text)):
    if text[i] == '(':
        stack.append(i)
    if text[i] == ')':
        index = stack.pop()
        print(text[index:i+1])
