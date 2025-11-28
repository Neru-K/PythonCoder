S = list(input())
k = []
v = []

for c in S:
    if k and c == k[-1]:
        v[-1] += 1

    else:
        k.append(c)
        v.append(1)

ans = 0

for j in range(len(k) - 1):
    prev = int(k[j])
    next = int(k[j + 1])

    if prev + 1 == next:
        ans += min(v[j], v[j + 1])

print(ans)
