tests = int(input())
 
for test in range(tests):
     
    input()
    array = []
    
    for row in range(8):
        
        string = input()
        array.append(string)
        
    for row in range(8):
        hash = []
        got = False
     
        for idx, char in enumerate(array[row]):
            if char == '#':
                hash.append(idx)
            if len(hash) == 2:
                got = True
                x1, x2 = hash
                middlePoint = x1 + (x2 - x1)//2
                
                height = row
                while x1 != x2:
                     x1 += 1
                     x2 -= 1
                     height += 1
                print(height + 1, middlePoint + 1 )
                break
        if got:
            break