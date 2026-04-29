from collections import Counter

N, K = map(int, input().split())

A = list(map(int, input().split()))

cnt = Counter(A)

sumsa = []
for a, c in cnt.items():
    sumsa.append(a * c)

sumsa.sort()

ans = 0

for j in range(len(sumsa) - K):
    ans += sumsa[j]

print(ans)
