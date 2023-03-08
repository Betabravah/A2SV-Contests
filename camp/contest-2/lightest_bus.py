from math import inf
tests = int(input())

for _ in range(tests):
    n = int(input())

    nums = list(map(int, input().split()))
    # print(nums)
    pre = [0] * (len(nums))

    p = 0
    for i in range(len(nums)):
        p += nums[i]
        pre[i] = p
    
    weight = pre[min(n-1, 11)]
    for i in range(12, len(pre), 6):
        weight = min(weight, pre[min(i + 11, n - 1)] - pre[i-1])

    print(weight)