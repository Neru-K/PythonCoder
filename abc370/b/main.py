N = int(input())

A = []

for _ in range(N):

    lst = list(map(int, input().split()))
    A.append(lst)

i = 0

for j in range(N):
    if i >= j:
        i = A[i][j] - 1
    else:
        i = A[j][i] - 1

print(i + 1)