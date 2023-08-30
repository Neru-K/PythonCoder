N, Q = map(int, input().split())

LRT = [list(map(int, input().split())) for _ in range(Q)]

result = [0] * N

for i in range(Q):
    for j in range(LRT[i][0] - 1, LRT[i][1]):
        result[j] = LRT[i][2]

for r in result:
    print(r)
