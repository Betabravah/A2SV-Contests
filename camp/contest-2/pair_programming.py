n, k = list(map(int, input().split()))

a = list(map(int, input().split()))

a.sort()
# print(a)
left = 0
mid = (2**n) // 2
time = 0
while k > 0:
    time += a[mid-1] * (min(k, mid - left))
    k -= (min(k, mid - left))
    left = mid
    mid = left + (len(a) - left) // 2

print(time)