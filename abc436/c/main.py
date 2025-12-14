N, M = map(int, input().split())

exist = set()

ans = 0

for i in range(M):
    R, C = map(int, input().split())
    R2, C2 = (R + 1) // 2, (C + 1) // 2

    if not (R2, C2) in exist:
        ans += 1
        exist.add((R2, C2))

print(ans)
