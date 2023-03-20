command = int(input())
x = 0
stack = [1]
for _ in range(command):
    com = input().split()
    if com[0] == 'add':
        x += stack[-1]
    elif com[0] == 'for':
        nested = stack[-1] * int(com[1])
        stack.append(min(nested, 2**32))
    elif com[0] == 'end':
        # x += stack[-1]
        stack.pop()
    if x > (2**32 - 1):
        print('OVERFLOW!!!')
        break
else:
    print(x)

    