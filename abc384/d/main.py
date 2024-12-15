N, S = map(int, input().split())
A = list(map(int, input().split()))

ruisekiwa = []

for i in range(N * 3):
    if i == 0:
        ruisekiwa.append(A[i])
    else:
        idx = i // N
        ruisekiwa.append(ruisekiwa[idx - 1] + A[idx])