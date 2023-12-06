N, K = map(int, input().split())
A = list(map(int, input().split()))

# カウント
cnt = {}
for a in A:
    if a in cnt:
        cnt[a] += 1
    else:
        cnt[a] = 1

v = sorted(cnt.values())

if len(v) <= K:
    ans = 0
else:
    ans = sum(v[: len(v) - K])

print(ans)
