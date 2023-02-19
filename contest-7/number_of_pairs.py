n = int(input())
boys = list(map(int, input().split()))
 
m = int(input())
girls = list(map(int, input().split()))
 
boys.sort()
girls.sort()
 
pairs = 0
boy = girl = 0
while boy < n and girl < m:
    if abs(boys[boy] - girls[girl]) <= 1:
        pairs += 1
        boy += 1
        girl += 1
    else:
        if boys[boy] < girls[girl]:
            boy += 1
        else:
            girl += 1
print(pairs)