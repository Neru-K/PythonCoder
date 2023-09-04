N, D = map(int, input().split())

XY = [list(map(int, input().split())) for _ in range(N)]

count = 0

for i in range(N):
    X = XY[i][0]
    Y = XY[i][1]
    if (X**2 + Y**2) ** 0.5 <= D:
        count += 1

print(count)
