tests = int(input())
 
for test in range(tests):
    len1, wid1 = list(map(int, input().split()))
    len2, wid2 = list(map(int, input().split()))
 
    max1 = max(len1, wid1)
    max2 = max(len2, wid2)
 
    min1 = min(len1, wid1)
    min2 = min(len2, wid2)    
 
    if max1 == max2 and max1 == min1 + min2:
        print('YES')
    else:
        print('NO')