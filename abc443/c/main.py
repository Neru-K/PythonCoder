N, T = map(int, input().split())
A = list(map(int, input().split()))

open = 0
ans = 0

if len(A) == 0:
    print(T)
    exit()

for i in range(N):
    if open < A[i]:
        ans += A[i] - open

        open = A[i] + 100

print(ans + max(0, T - open))
