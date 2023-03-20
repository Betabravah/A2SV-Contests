tests = int(input())

for _ in range(tests):
    n, h = map(int, input().split())

    nums = list(map(int, input().split()))

    low, high = 1, h
    while low <= high:
        mid = low + (high - low) // 2
        
        score = 0
        for i in range(len(nums)-1):
            score += min(mid, nums[i+1] - nums[i])
        score += mid

        if score >= h:
            high = mid - 1
        else:
            low = mid + 1

    print(low)
