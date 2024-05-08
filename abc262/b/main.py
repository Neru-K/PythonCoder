N, M = map(int, input().split())

edges = {}


for i in range(M):
    U, V = map(int, input().split())
    if U not in edges:
        edges[U] = set([V])
    else:
        edges[U].add(V)

    if V not in edges:
        edges[V] = set([U])
    else:
        edges[V].add(U)

count = 0
done = set()

for a in edges: #
    for b in edges[a]:
        for c in edges[b]:
            abc = [a,b,c]
            abc.sort()
            t = tuple(abc)
            if t not in done:
                done.add(t)
                if a in edges[b] and b in edges[c] and c in edges[a]:
                    count += 1

print(count)