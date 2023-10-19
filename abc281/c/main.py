N, T = map(int, input().split())
A = list(map(int, input().split()))
sm = sum(A)
rem = T // sm
count = 0

for i in range(N):
    if T - A[i] > 0:
        T -= A[i]
        count += 1

print(str((count % N) + 1) + " " + str(T))
