H, W = map(int, input().split())

for i in range(H):
    lst = []

    for j in range(W):
        if i == 0 or i == H - 1:
            lst.append("#")
        elif j == 0 or j == W - 1:
            lst.append("#")
        else:
            lst.append(".")

    print(*lst, sep="")
