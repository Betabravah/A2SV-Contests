n = int(input())
nums = list(map(int, input().split()))
nums.sort()
 
start = 0
maxLen = 0
for end in range(len(nums)):
    while nums[end] > nums[start] + 5:
        start += 1
    maxLen = max(maxLen, end - start + 1)
print(maxLen)