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

# 入力
N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]

# クエリの処理
uf = unionfind(N)
for tp, u, v in queries:
	if tp == 1:
		uf.unite(u, v)
	if tp == 2:
		if uf.same(u, v):
			print("Yes")
		else:
			print("No")

N = int(input())

for i in range(N):
    