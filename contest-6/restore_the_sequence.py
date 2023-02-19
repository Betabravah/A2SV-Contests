tests = int(input())
 
for test in range(tests):
    n = int(input())
    seq = list(map(int, input().split()))
 
    favSeq = []
    left, right = 0, n - 1
    while left <= right:
        if left < right:
            favSeq.append(seq[left])
            favSeq.append(seq[right])
        else:
            favSeq.append(seq[left])
        left += 1
        right -= 1
    print(*favSeq)