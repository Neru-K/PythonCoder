N, L, R = map(int, input().split())
S = input()

d = {}

for i in range(len(S)):
    if S[i] in d:
        d[S[i]].append(i)
    else:
        d[S[i]] = [i]

ans = 0

for v in d.values():
    for i in range(0, len(v) - 1):
        for j in range(i + 1, len(v)):
            diff = v[j] - v[i]
            if diff > R:
                break
            if L <= diff:
                ans += 1

print(ans)
