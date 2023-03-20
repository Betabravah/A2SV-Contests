n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

happy = 0
if len(nums) == 1:
    happy = nums[-1] * min(k, m)
else:
    prod = m // (k + 1)
    rem = m % (k + 1)
    happy += (prod * k + rem) * nums[-1]
    happy += prod * nums[-2]

print(happy)