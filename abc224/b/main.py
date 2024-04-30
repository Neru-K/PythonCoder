H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

list_i = []
list_j = []

for i in range(H - 1):
    for i2 in range(i + 1, H):
        list_i.append((i, i2))

for j in range(W - 1):
    for j2 in range(j + 1, W):
        list_j.append((j, j2))

for i in range(len(list_i)):
    for j in range(len(list_j)):
        i1 = list_i[i][0]
        i2 = list_i[i][1]
        j1 = list_j[j][0]
        j2 = list_j[j][1]

        if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
            print("No")
            exit()

print("Yes")