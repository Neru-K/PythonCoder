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


N, M = map(int, input().split())
uf = unionfind(N)
friends = set()

for i in range(M):
    A, B = map(int, input().split())
    uf.unite(A, B)

lst_friends = list(friends)
max_size = 0

for j in range(1, N + 1):
    size = uf.size[uf.root(j)]
    if size > max_size:
        max_size = size

print(max_size)
