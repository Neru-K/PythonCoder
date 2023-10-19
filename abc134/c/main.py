N = int(input())

A = []
max = 0
next = 0

for i in range(N):
    A.append(int(input()))
    if A[i] > max:
        max = A[i]
    elif A[i] > next:
        next = A[i]

for j in range(N):
    if A[j] == max:
        print(next)
    else:
        print(max)
