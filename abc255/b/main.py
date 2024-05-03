import math

N, K = map(int,input().split())
A = list(map(int,input().split()))
XY = []
distances = []

for i in range(N):
    X, Y = map(int, input().split())
    XY.append((X,Y))

for i in range(N):
    mn = 999999999999999999999999999
    for j in range(K):

        X1 = XY[i][0]
        Y1 = XY[i][1]
        X2 = XY[A[j] - 1][0]
        Y2 = XY[A[j] - 1][1]
        distance = ((X1 - X2) ** 2) + ((Y1 - Y2) ** 2)

        if distance < mn:
            mn = distance

    distances.append(mn)

print(math.sqrt(max(distances)))