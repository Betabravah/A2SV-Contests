tests = int(input())
 
for _ in range(tests):
    mat = []
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
 
    mat.append(r1)
    mat.append(r2)
 
 
    for i in range(4):
        if mat[0][0] < mat[0][1] and mat[1][0] < mat[1][1] and mat[0][0] < mat[1][0] and mat[0][1] < mat[1][1]:
                print("YES")
                break
        else:
            tmp = mat[1][0]
            mat[1][0] = mat[1][1]
            mat[1][1] = mat[0][1]
            mat[0][1] = mat[0][0]
            mat[0][0] = tmp
    else:
        print("NO")