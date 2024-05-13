import copy

H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        Acopy = copy.deepcopy(A)
        for i in range(H):
            for j in range(W):
                Acopy[i][j] = A[(i + h) % H][(j + w) % W]

        if Acopy == B:
            print("Yes")
            exit()

print("No")
