N, M, T = map(int,input().split())
A = list(map(int, input().split()))

Xs = [0] * N

for i in range(M):
    X, Y = map(int, input().split())
    Xs[X - 1] = Y

for i in range(N - 1):
    T -= A[i]
    if T <= 0:
        print("No")
        exit()

    T += Xs[i + 1]

print("Yes")