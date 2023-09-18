N, K, Q = map(int, input().split())

A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    if A[l - 1] < N:
        if A[l - 1] + 1 not in A:
            A[l - 1] = A[l - 1] + 1

result = list(map(str, A))

print(" ".join(result))
