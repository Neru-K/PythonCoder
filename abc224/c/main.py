from itertools import combinations

N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0

for (x1, y1), (x2, y2), (x3, y3) in combinations(coordinates, 3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if area != 0:
        ans += 1

print(ans)