N, K, X = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)

sum = 0

for i in range(N - K, N):

    sum += A[i]
    if sum >= X:
        print(i + 1)
        exit()

print(-1)
