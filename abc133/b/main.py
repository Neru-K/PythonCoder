N, D = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(N)]

X.append(X[0])

count = 0

for i in range(N):
    for j in range(i + 1, N):
        sum = 0

        for k in range(D):
            sum += (X[i][k] - X[j][k]) ** 2

        if sum**0.5 == int(sum**0.5):
            count += 1

print(count)
