import sys

sys.setrecursionlimit(120000)

N = int(input())
X, Y = map(str, input().split())

visited = set()
edges = {}

for i in range(N):
    S, T = map(str, input().split())

    if S in edges:
        edges[S].add(T)
    else:
        edges[S] = set()
        edges[S].add(T)
		
def graph(s):
    if s in edges:
        for key in edges[s]:
            if key == Y:
                print("Yes")
                exit()

            if key not in visited:
                visited.add(key)
                graph(key)

graph(X)
print("No")
