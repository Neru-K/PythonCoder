H, W = map(int, input().split())
U, D, L, R = 999, -1, 999, -1

S = []

for i in range(H):
    row = input()
    S.append(row)
    for j in range(W):
        if row[j] == "#":
            U = min(U, i)
            L = min(L, j)
            D = max(D, i)
            R = max(R, j)

for i in range(U, D + 1):
    for j in range(L, R + 1):
        if S[i][j] == ".":
            print(i + 1, j + 1)
