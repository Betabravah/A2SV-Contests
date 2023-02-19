tests = int(input())
 
for test in range(tests):
    nums = list(map(int, input().split()))
    minn = min(nums)
    maxx = max(nums)
 
    for num in nums:
        if num != minn and num != maxx:
            print(num)
            break