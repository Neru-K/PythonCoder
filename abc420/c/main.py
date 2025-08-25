N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minAB = 0

for n in range(N):
    minAB += min(A[n], B[n])

for i in range(Q):
    c, X, V = map(str, input().split())
    X = int(X)
    V = int(V)
    idx = X - 1

    min_prev = min(A[idx], B[idx])

    if c == "A":
        A[idx] = V
    else:
        B[idx] = V

    min_after = min(A[idx], B[idx])
    minAB += min_after - min_prev

    print(minAB)
