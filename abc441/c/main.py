N, K, X = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

sum = 0

for i in range(K):
    sum += A[i]
    if sum >= X:
        print(i + 1 + (N - K))
        exit()

print(-1)
