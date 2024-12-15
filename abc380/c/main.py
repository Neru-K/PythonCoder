N, K = map(int, input().split())
S = input()
S = "0" + S + "0"
ans = ""

L = []
R = []

ans = []

for i in range(1, N + 2):
    if S[i - 1] == "0" and S[i] == "1":
        L.append(i - 1)
    elif S[i - 1] == "1" and S[i] == "0":
        R.append(i - 2)

idx_l = 0
idx_r = 0

for j in range(N):
    if 