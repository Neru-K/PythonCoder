N = int(input())

XYs = []

for i in range(N):
    X, Y = map(int, input().split())
    XYs.append([X, Y])

XYs.sort(key=lambda x: x[0])

minY = N + 1

ans = 0

for x, y in XYs:
    if y < minY:
        minY = y
        ans += 1

print(ans)
