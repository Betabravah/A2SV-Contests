contests = int(input())
x =input().split()
scores = list(map(int, x))
 
ctr = 0
minn = maxx = scores[0]
for i in range(1, len(scores)):
    if scores[i] < minn:
        minn = scores[i]
        ctr += 1
    elif scores[i] > maxx:
        maxx = scores[i]
        ctr += 1
 
print(ctr)