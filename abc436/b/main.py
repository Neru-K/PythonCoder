N = int(input())

grid = []

for i in range(N):
    grid2 = []
    for j in range(N):
        grid2.append(0)

    grid.append(grid2)

r, c = 0, N // 2
grid[r][c] = 1

for k in range(N * N - 1):
    r2, c2 = (r - 1) % N, (c + 1) % N
    if grid[r2][c2] == 0:
        grid[r2][c2] = k + 2
    else:
        r2, c2 = (r + 1) % N, c
        grid[r2][c2] = k + 2

    r, c = r2, c2


for l in range(N):
    print(*grid[l])
