n, k = map(int, input().split())

nums = list(map(int, input().split()))


def play(p1, i1, p2, i2):
    if p1 - p2 > k:
        return [[p1, i1]]
    elif  p2 - p1 > k:
        return [[p2, i2]]
    else:
        return [[p1, i1], [p2, i2]]
    
for i in range(0, len(nums) - 1, 2):
    nums[i] = play(nums[i], i, nums[i + 1], i+1)

# print(nums)
winners = []
for i in range(0, len(nums) - 2, 4):
    for p1 in nums[i]:
        for p2 in nums[i+2]:
            winners.append(play(p1[0], p1[1], p2[0], p2[1]))

# print(winners)
win = set()
for w in winners:
    for i in w:
        win.add(i[1]+1)

print(*win)