tests = int(input())

for _ in range(tests):
    students, outlets = list(map(int, input().split()))

    out = list(map(int, input().split()))
    out.sort(reverse=True)
    got = False
    if students <= 2:
        print(0)
    else:
        # print(out)
        pre = 2
        count = 0
        for i, o in enumerate(out):
            pre += o - 1
            count += 1
            if pre >= students:
                got = True
                break
            # out[i] = pre
        
        if got:
            print(count)
        else:
            print(-1)
            

        
