N = int(input())

xy = []

for i in range(N):
    xy.append(list(map(int,input().split())))

max = 0

for i in range(N):
    x1, y1 = xy[i][0],xy[i][1]
    for j in range(i + 1,N):
        x2,y2 = xy[j][0],xy[j][1]

        len = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        if len > max:
            max = len

print(max)