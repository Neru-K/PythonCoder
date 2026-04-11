T, X = map(int, input().split())

A = list(map(int, input().split()))

prev = 0

for i in range(T + 1):

    if i == 0 or abs(A[i] - prev) >= X:
        print(str(i), str(A[i]))
        prev = A[i]
