tests = int(input())
 
for test in range(tests):
    length, start = input().split()
    length = int(length)
    string = input()
    
    stack = []
    seconds = 0
    for position in range(len(string)*2):
        position = position % len(string)
        if string[position] == start:
            stack.append(string[position])
        
        
        elif string[position] == 'g':
            sec = 0
            while stack:
                sec += 1
                stack.pop()
            seconds = max(seconds, sec)
        else:
            if stack:
                stack.append(string[position])
 
    print(seconds)