N, M = map(int, input().split())

dp = [[0] * M for _ in range(N)]

    
for i in range(N):
    S = input()
    for j in range(M):
        if i == 0:
            if S[j] == "o":
                dp[0][j] = 1

        else:
            if S[j] == "x":
                dp[i][j] = dp[i - 1][j]
            else:
                if dp[][]

