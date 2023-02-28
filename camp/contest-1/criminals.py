test = int(input())

for _ in range(test):
    n = int(input())

    nums = list(map(int, input().split()))

    left = 0
    for i in range(n):
        if nums[i] > 0:
            left = i
            break
    else:
        left = n

    zeroes = 0
    nonZeroes = 0
    while left < n - 1:
        if nums[left] == 0:
            zeroes += 1
        else:
            nonZeroes += nums[left]
        left += 1
    print(zeroes + nonZeroes)
    

