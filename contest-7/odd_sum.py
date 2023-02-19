n = int(input())
nums = list(map(int, input().split()))
 
nums.sort()
total = sum(nums)
 
half = 0
for i in range(n):
    half += nums[i]
 
if 2 * half != total:
    print(*nums)
else:
    print(-1)