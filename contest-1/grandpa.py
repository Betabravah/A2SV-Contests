stones = input().split(' ')
uniques = []
ctr = 0
 
for i in stones:
    if i not in uniques:
        ctr += 1
        uniques.append(i)
 
    if ctr == 5:
        break
if ctr == 5:
    print('YES')
else:
    print('NO')
 