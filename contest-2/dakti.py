
tests = int(input())
 
for i in range(tests):
    words = input().split()
    
    _dict = {}
    
    for word in words:
        letters = []
        digits = []
        for char in word:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        digit = int(''.join(digits))
        word = ''.join(letters)
        _dict[digit] = word
 
    _dict = sorted(_dict.items())
    _list = [x[1] for x in _dict]
 
    
    print(' '.join(_list))