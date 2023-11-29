""" 20231130
Atcoder Problemsのバチャを立てる拡張機能を作り始めた。
妻とタンメンを食べて、近くの書店兼喫茶店でコーヒーを飲む """

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

maxCount = 0

for i in range(N):
    count = 1

    L = i
    R = i + 1

    while i < N - 1 and A[R[i] + 1] < A[i] + M:
        R[i] += 1
        count += 1

    if count > maxCount:
        maxCount = count

print(maxCount)
