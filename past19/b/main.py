N = int(input())
A = list(map(int, input().split()))

ain = 0
aout = 0

for i in range(1, N):
    if A[i] > A[i - 1]:
        aout += A[i] - A[i - 1]
    else:
        ain += A[i - 1] - A[i]

print(aout,ain)