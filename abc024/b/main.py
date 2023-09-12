N, T = map(int, input().split())

A = [int(input()) for _ in range(N)]

A.append(A[N - 1] + T)

spend = []

open = 0

for i in range(1, N + 1):
    spend.append(A[i] - A[i - 1])

for j in range(N):
    if spend[j] > T:
        open += T
    else:
        open += spend[j]

print(open)
