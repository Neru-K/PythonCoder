N = int(input())

A = [0] * N
count = 0

for i in range(N):
    A[i] = int(input())

    if A[i] < i + 1 and A[i] == A[A[i] - 1]:
        count += 1

print(count)
