n, d = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
left, right = 0, len(nums) - 1
ctr = 0
while left <= right:
    if nums[right] > d:
        ctr += 1
        right -= 1
        continue
    if right > left:
        count = 2
        while left < right-1 and count * nums[right] <= d:
            left += 1
            count += 1 
        if count * nums[right] > d:
            ctr += 1
    left += 1
    right -= 1

print(ctr)