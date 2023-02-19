tests = int(input())
 
for _ in range(tests):
    length, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
 
    prev = count = start = 0
    cur = 1
    while cur < length:
        if arr[cur]*2 <= arr[prev]:
            start = cur
        if cur - start >= k:
            count += 1
        cur += 1
        prev += 1
    print(count)