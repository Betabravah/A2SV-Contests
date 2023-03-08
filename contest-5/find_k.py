tests = int(input())
from collections import defaultdict

for i in range(tests):
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))

    pos = defaultdict(int)
    neg = defaultdict(int)

    for num in nums:
        offset1 = k + num
        if offset1 in pos:
            print('Yes')
            break
        else:
            pos[num] += 1
        
        offset2 = num - k
        if offset2 in neg:
            print('Yes')
            break
        else:
            neg[num] += 1

    else:
        print('No')
