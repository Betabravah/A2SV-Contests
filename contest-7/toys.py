from collections import defaultdict
toys, choice = list(map(int, input().split()))
price = list(map(int, input().split()))
 
andyToys = defaultdict(int)
for i in range(choice):
    andyToys[(input())] += 1
 
price.sort()
andyToys = sorted(andyToys.items(), key=lambda x:x[1])
 
minPrice = maxPrice = 0
left, right = 0, toys - 1
for i in range(len(andyToys)-1, -1, -1):
    minPrice += (price[left] * andyToys[i][1])
    maxPrice += (price[right] * andyToys[i][1])
 
    left += 1
    right -= 1
 
print(minPrice, maxPrice)