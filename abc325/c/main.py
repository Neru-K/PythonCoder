class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            # Path compression
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self, u, v):
        return self.root(u) == self.root(v)


def in_bound(r, c, H, W):
    return 0 <= r < H and 0 <= c < W


# 入力
H, W = map(int, input().split())
grid_nums = H * W
uf = unionfind(grid_nums)
directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

count = 0

S = [input() for _ in range(H)]

for i in range(grid_nums):
    r = i // W
    c = i % W
    if S[r][c] == "#":
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if in_bound(nr, nc, H, W) and S[nr][nc] == "#":
                uf.unite(i, nr * W + nc)

count = set()
for j in range(grid_nums):
    if S[j // W][j % W] == "#":
        count.add(uf.root(j))

print(len(count))
