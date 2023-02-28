from math import inf
tests = int(input())

for _ in range(tests):
    n, m = list(map(int, input().split()))
    string = input()

    nums = []
    for i in string:
        nums.append(int(i))

    left = []
    latestOne = -inf
    for i in range(n):
        left.append(latestOne)
        if nums[i] == 1:
            latestOne = i


    right = [0] * n
    latestOne = inf
    for i in range(n-1, -1, -1):
        right[i] = latestOne
        if nums[i] == 1:
            latestOne = i

    for i in range(n):
        if nums[i] == 0:
            lateLeft, lateRight = (i - left[i]), (right[i] - i)
            if lateLeft != lateRight:
                distance = min(lateLeft, lateRight)

                if distance <= m:
                    nums[i] = 1

    nums = list(map(str, nums))
    print(''.join(nums))

