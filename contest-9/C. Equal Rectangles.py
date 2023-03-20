tests = int(input())
for _ in range(tests):
    n = int(input())

    nums = list(map(int, input().split()))

    nums.sort()

    left , right = 0, len(nums) - 1

    area = None
    while left < right:
        if nums[left] != nums[left+1] or nums[right] != nums[right-1]:
            print('NO')
            break
        if not area:
            area = nums[left] * nums[right]
            continue
        
        new_area = nums[left] * nums[right]

        if new_area != area:
            print('NO')
            break

        left += 2
        right -= 2

    else:
        print('YES')


