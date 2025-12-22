N, M = map(int, input().split())

set_grid = set()
direction = [(0, 0), (0, 1), (1, 1), (1, 0)]

ans = 0


def ok(R, C):
    for j in range(4):
        now = (R + direction[j][0], C + direction[j][1])
        if now in set_grid:
            return False

    return True


for i in range(M):
    R, C = map(int, input().split())

    if ok(R, C):
        for k in range(4):
            set_grid.add((R + direction[k][0], C + direction[k][1]))
        ans += 1

print(ans)
