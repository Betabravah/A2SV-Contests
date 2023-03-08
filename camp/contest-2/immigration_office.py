length = int(input())

names = list(input().split())
names.sort()


q = int(input())
for i in range(q):
    name = input()
    
    low, high = 0, len(names)-1
    while low <= high:
        mid = low + (high - low) // 2
        if names[mid] > name:
            high = mid - 1
        elif names[mid] == name:
            break
        else:
            low = mid + 1

    print(low)
