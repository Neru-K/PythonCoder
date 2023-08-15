N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(M)]

dict = {}

for i in range(M):
    for j in range(N - 1):
        if a[i][j] in dict:
            if a[i][j + 1] not in dict[a[i][j]]:
                dict[a[i][j]].append(a[i][j + 1])
        else:
            dict[a[i][j]] = [a[i][j + 1]]

        if a[i][j + 1] in dict:
            if a[i][j] not in dict[a[i][j + 1]]:
                dict[a[i][j + 1]].append(a[i][j])
        else:
            dict[a[i][j + 1]] = [a[i][j]]
