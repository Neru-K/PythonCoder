N, M = map(int, input().split())


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


# クエリの処理
uf = unionfind(N)

for i in range(M):
    u, v = map(int, input().split())
    uf.unite(u, v)

count = sum(1 for x in uf.par if x == -1)
print(count - 1)
