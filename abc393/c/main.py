N, M = map(int, input().split())

set_uv = set()

for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        continue
    if u > v:
        u, v = v, u

    set_uv.add((u, v))

print(M - len(set_uv))
