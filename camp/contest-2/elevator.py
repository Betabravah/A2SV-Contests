tests = int(input())

for _ in range(tests):
    w, e, c = list(map(int, input().split()))


    def climb(f, c):
        if f == 4:
            return 0
        else:
            walk = w + climb(f+1, c)
            ride = ((abs(c - f) + 1) * e) + climb(f+1, f+1)

            return min(walk, ride)

    print(climb(0, c))
