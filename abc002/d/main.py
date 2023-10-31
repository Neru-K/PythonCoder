N, M = map(int, input().split())
relation = [[False] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    relation[x - 1][y - 1] = True
    relation[y - 1][x - 1] = True

answer = 0

for bit in range(1 << N):
    members = []
    for i in range(N):
        if bit & (1 << i):
            members.append(i)

    ok = True
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            if not relation[members[i]][members[j]]:
                ok = False
                break
        if not ok:
            break

    if ok:
        answer = max(answer, len(members))

print(answer)
