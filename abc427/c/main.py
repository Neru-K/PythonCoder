from itertools import product

N, M = map(int, input().split())

list_uv = []

for i in range(M):
    u, v = map(int, input().split())
    list_uv.append((u, v))

INF = 1 << 60
min_count = INF

for pro in product((0, 1), repeat=N):
    delete_count = 0
    for u, v in list_uv:
        if pro[u - 1] == pro[v - 1]:
            delete_count += 1

    if min_count > delete_count:
        min_count = delete_count

print(min_count)
