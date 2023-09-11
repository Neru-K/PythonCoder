N, H, X = map(int, input().split())
P = list(map(int, input().split()))

min = 1000
idx = -1

for i in range(N):
    if H + P[i] >= X:
        if P[i] < min:
            min = P[i]
            idx = i

print(idx + 1)
