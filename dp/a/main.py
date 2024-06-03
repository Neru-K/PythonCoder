N = int(input())
h = list(map(int,input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(1,N):
    hi = abs(h[i] - h[i - 1])
    hj = hi
    if i % 2 == 0:
        hj = abs(h[i] - h[i - 2])

    dp[i] = min(hi + dp[i - 1], hj + dp[i - 2])

print(dp[N-1])