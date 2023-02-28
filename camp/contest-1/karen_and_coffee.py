n, k, q = list(map(int, input().split()))

nums = [0] * 200002
for i in range(n):
    l, r = list(map(int, input().split()))

    nums[l] += 1
    nums[r + 1] -= 1

prefix = [0] * 200002
for i in range(1,200002):
    prefix[i] = (prefix[i - 1] + nums[i])

admiss = [0] * 200002
for i in range(1, 200002):
    if prefix[i] >= k:
        admiss[i] = (admiss[i-1] + 1)
    else:
        admiss[i] = (admiss[i-1])

for i in range(q):
    a, b = list(map(int, input().split()))
    print(admiss[b] - admiss[a-1])