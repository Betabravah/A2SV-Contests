rows, cols, k = map(int, input().split())

mat = []
for r in range(rows):
    mat.append(input())

num_ways = 0

# check for rows
for rIdx, row in enumerate(mat):
    adjacent = 0
    for cIdx, col in enumerate(row):
        if col == ".":
            adjacent += 1
        else:
            adjacent = 0

        if adjacent >= k:
            num_ways += 1

# check for columns
for cIdx in range(cols):
    adjacent = 0
    for row in mat:
        if row[cIdx] == '.':
            adjacent += 1
        else:
            adjacent = 0

        if adjacent >= k:
            num_ways += 1

if k == 1:
    num_ways //= 2

print(num_ways)
