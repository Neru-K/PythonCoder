N, K = map(int, input().split())
S = input()
S = "0" + S + "0"
ans = ""

L = []
R = []

ans = [0] * N

for i in range(1, N + 2):
    if S[i - 1] == "0" and S[i] == "1":
        L.append(i - 1)
    elif S[i - 1] == "1" and S[i] == "0":
        R.append(i - 2)

diff = R[K - 1] - L[K - 1]
L[K - 1] = R[K - 2] + 1
R[K - 1] = L[K - 1] + diff

idx = 0

for j in range(len(L)):
    for k in range(L[j], R[j] + 1):
        ans[k] = 1

print(*ans, sep='')