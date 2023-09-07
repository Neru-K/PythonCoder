N, M = map(int, input().split())

A = list(map(int, input().split()))

sum = sum(A)
less = sum / (4 * M)
count = 0

for i in range(N):
    if A[i] >= less:
        count += 1

if count >= M:
    print("Yes")
else:
    print("No")
