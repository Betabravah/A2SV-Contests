n = int(input())
nums = list(map(int, input().split()))

wube = henok = 0
turn = 'wube'
left, right = 0, n - 1
while left <= right:
    if nums[left] > nums[right]:
        if turn == 'wube':
            wube += nums[left]
            turn = 'henok'
        else:
            henok += nums[left]
            turn = 'wube'
        left += 1
    else:
        if turn == 'wube':
            wube += nums[right]
            turn = 'henok'
        else:
            henok += nums[right]
            turn = 'wube'
        right -= 1

print(wube, henok)