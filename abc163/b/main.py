N, M = map(int, input().split())
A = list(map(int, input().split()))

study = N - sum(A)

if study >= 0:
    print(study)
else:
    print(-1)
