n = int(input())

for _ in range(n):
    working = []
    string = input()
    length = len(string)

    left = right = 0
    count = 0
    working = set()
    while right < len(string):
        if string[left] == string[right]:
            count += 1
            
        else:
            if (count) % 2:
                working.add(string[left])
            left = right
            count = 1

        right += 1    

    if count % 2:
        working.add(string[-1])

    working = sorted(working)
    # print(working)
    print(''.join(working))