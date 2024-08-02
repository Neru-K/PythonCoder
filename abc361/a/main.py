N, K, X = map(int,input().split())

A = list(map(int, input().split()))
B = []

for i in range(N):
    if i == K  - 1:
        B.append(A[i])
        B.append(X)
    else:
        B.append(A[i])

print(*B)