words = int(input())
 
pattern = []
change = []
for i in range(words):
    new_word = input()
 
    for index in range(len(new_word)):
        try:
            if pattern[index] == '!':
                continue
            elif pattern[index] == '?':
                if pattern[index] != '?':
                    pattern[index] = new_word[index]
                    change.append(False)
                else:
                    pattern[index] = new_word[index]
            elif pattern[index] != new_word[index] and new_word[index] != '?':
                pattern[index] = '!'
        except:
            pattern.append(new_word[index])
 
for index in range(len(pattern)):
    if pattern[index] == '!':
        pattern[index] = '?'
    elif pattern[index] == "?":
        pattern[index] = 'x'
 
print(''.join(pattern))