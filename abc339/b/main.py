H, W, N = map(int, input().split())

dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
dir_idx = 0
grid = [["."] * W for _ in range(H)]
pos = [0, 0]

for i in range(N):
    x = pos[0]
    y = pos[1]

    if grid[y][x] == ".":
        dir_idx = (dir_idx + 1) % 4
        grid[y][x] = "#"
        pos[0] = (pos[0] + dirs[dir_idx][0]) % W
        pos[1] = (pos[1] + dirs[dir_idx][1]) % H

    else:
        dir_idx = (dir_idx - 1) % 4
        grid[y][x] = "."
        pos[0] = (pos[0] + dirs[dir_idx][0]) % W
        pos[1] = (pos[1] + dirs[dir_idx][1]) % H

result = ""

for i in range(H):
    if i > 0:
        result = result + "\n"

    result += "".join(grid[i])

print(result)