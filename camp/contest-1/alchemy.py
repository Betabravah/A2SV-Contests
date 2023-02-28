n = int(input())
 
nums = list(map(int, input().split()))
left, right = 0, n-1
 
ed = alp = 0
edc = alpc = 0
while left <= right:
    if left == right:
        if ed <= alp:
            ed += nums[left]
            edc += 1
            left += 1
        else:
            alp += nums[right]
            alpc += 1
            right -= 1
    else:
        if ed > alp:
            alp += nums[right]
            alpc += 1
            right -= 1
        else:
            ed += nums[left]
            edc += 1
            left += 1
 
print(edc, alpc)