X, K = map(int, input().split())
#list_s = list(map(int, input().split()))
#N, M = map(int, input().split())
#A = [list(map(int, input().split())) for _ in range(N)]

for i in range(K):
    digit = 10 ** (i + 1)

    X /= digit
    X += 0.01
    X = round(X, 0) * digit

print(int(X))