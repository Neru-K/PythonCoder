N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

for i in range(N - 1, -1, -1):
    if i + 1 == A[i]:
        ans[i] = A[i]
    else:
        ans[i] = ans[A[i] - 1]

print(*ans, sep=" ")
