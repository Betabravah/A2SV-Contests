from collections import defaultdict
from math import inf
tests = int(input())

for _ in range(tests):
    string = input()

    left = 0
    ctr = defaultdict(int)
    minLen = inf
    for right in range(len(string)):
        ctr[string[right]] += 1
        while len(ctr) == 3:
            length = (ctr['1'] + ctr['2'] + ctr['3'])
            minLen = min(minLen, length)
            ctr[string[left]] -= 1
            if ctr[string[left]] == 0:
                ctr.pop(string[left])
            left += 1

    if minLen == inf:
        print(0)
    else:            
        print(minLen)
