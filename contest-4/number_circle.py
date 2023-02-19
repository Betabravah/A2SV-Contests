length = int(input())
nums = list(map(int, input().split()))
 
nums.sort()
if nums[-2] + nums[0] > nums[-1]:
    print("YES")
    print(*nums)
else:
    if nums[-2] + nums[-3] > nums[-1]:
        nums[-2], nums[-1] = nums[-1], nums[-2]
        print("YES")
        print(*nums)
    else:
        print("NO")