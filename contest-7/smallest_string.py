tests = int(input())
for _ in range(tests):
    len1, len2, k = list(map(int, input().split()))
    str1 = list(input())
    str2 = list(input())
 
    str1.sort()
    str2.sort()
 
    k1 = k2 = k
    ptr1 = ptr2 = 0
    united = []
    while ptr1 < len1 and ptr2 < len2:
        if k1 and str1[ptr1] <= str2[ptr2]:
            united.append(str1[ptr1])
            ptr1 += 1
            k1 -= 1
            k2 = k
        elif k2 and str2[ptr2] < str1[ptr1]:
            united.append(str2[ptr2])
            ptr2 += 1
            k2 -= 1
            k1 = k
        elif k1:
            united.append(str1[ptr1])
            ptr1 += 1
            k1 -= 1
            k2 = k
        elif k2:
            united.append(str2[ptr2])
            ptr2 += 1
            k2 -= 1
            k1 = k
 
    print(''.join(united))