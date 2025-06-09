H, W = map(int, input().split())
grid = []
top, right, bottom, left = H + 1, -1, -1, W + 1
whites_coodinates = []

for r in range(H):
    S = input()
    grid.append(S)

    for c in range(W):
        if S[c] == "#":
            if r < top:
                top = r
            if c > right:
                right = c
            if r > bottom:
                bottom = r
            if c < left:
                left = c
        elif S[c] == ".":
            whites_coodinates.append((r, c))

for i in range(len(whites_coodinates)):
    row = whites_coodinates[i][0]
    col = whites_coodinates[i][1]
    if row >= top and row <= bottom and col >= left and col <= right:
        print("No")
        exit()

print("Yes")
