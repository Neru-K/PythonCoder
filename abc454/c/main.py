import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

to = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append(B)

visited = [0] * N


def dfs(u):
    visited[u] = 1
    for v in to[u]:
        if visited[v] == 0:
            dfs(v)


dfs(0)

print(sum(visited))
