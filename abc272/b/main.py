N, M = map(int, input().split())

matrix = [[0] * N for _ in range(N)]


for m in range(M):
    row = list(map(int, input().split()))
    k = row[0]
    x = row[1:]

    for i in range(0, k):
        for j in range(i + 1, k):
            p1 = x[i] - 1
            p2 = x[j] - 1
            matrix[p1][p1] = 1
            matrix[p2][p2] = 1
            matrix[p1][p2] = 1
            matrix[p2][p1] = 1

result = "Yes"

for n in range(N):
    if 0 in matrix[n]:
        result = "No"
        break

print(result)
