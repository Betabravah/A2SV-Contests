lecture, secret = list(map(int, input().split()))
theorems = list(map(int, input().split()))
behavior = list(map(int, input().split()))
 
min_thm = 0
for i in range(lecture):
    if behavior[i] == 1:
        min_thm += theorems[i]
 
 
thm = 0
sec = secret
left = right = 0
while right < secret:
    if behavior[right] == 0:
        thm += theorems[right]
    right += 1
 
max_thm = thm
while right < lecture:
    if behavior[left] == 0:
        thm -= theorems[left]
    if behavior[right] == 0:
        thm += theorems[right]
 
    max_thm = max(max_thm, thm)
 
    left += 1
    right += 1
 
print(max_thm + min_thm)