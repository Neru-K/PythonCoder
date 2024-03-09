N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]


for i in range(N):
    result = []
    for j in range(N):
        if A[i][j] == 1:
            result.append(j + 1)
    print(*result)
