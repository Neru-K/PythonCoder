N, Q = map(int,input().split())
T = list(map(int,input().split()))

teeth = [1] * N

for i in range(Q):
    idx = T[i] - 1
    teeth[idx] = 1 if teeth[idx] == 0 else 0

count = 0

for i in range(N):
    if teeth[i] == 1:
        count += 1

print(count)