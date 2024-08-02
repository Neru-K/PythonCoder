N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

sumA = 0
sumB = 0

for i in range(N):
    sumA += A[i]
    sumB += B[i]

    if sumA > X or sumB > Y:
        print(i + 1)
        exit()

print(N)