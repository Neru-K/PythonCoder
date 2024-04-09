N = int(input())

XY = []
result = []

for i in range(N):
    X, Y = map(int,input().split())
    XY.append((X, Y))

for i in range(N):
    mx = -1
    mxidx = -1

    for j in range(N):
        if i == j:
            continue

        d = (XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2
        if d > mx:
            mx = d
            mxidx = j

    print(mxidx + 1)