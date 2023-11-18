N, M = map(int, input().split())
A = list(map(int, input().split()))

p = [0] * N
maxPoint = 0
maxPerson = 0

for i in range(M):
    p[A[i] - 1] += 1

    if p[A[i] - 1] > maxPoint:
        maxPoint = p[A[i] - 1]
        maxPerson = A[i]
    elif p[A[i] - 1] == maxPoint:
        if maxPerson > A[i]:
            maxPerson = A[i]

    print(maxPerson)
