N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * K

for a in A:
    cnt[a - 1] += 1

max_c = max(cnt)
ans = 0

for c in cnt:
    if c >= max_c - 1:
        ans += 1

print(ans)
