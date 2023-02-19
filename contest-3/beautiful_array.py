length = int(input())
 
nums = list(map(int, input().split()))
 
pos = []
neg = []
zero = []
for num in nums:
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero.append(num)
 
print(1, neg.pop())
if len(pos) != 0:
    print(len(pos), *pos)
else:
    print(2, neg.pop(), neg.pop())
 
print(len(neg) + len(zero), end=' ')
print(*zero, end=' ')
print(*neg)