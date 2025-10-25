N, M = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)

for i in range(N):
    if sumA - A[i] == M:
        print("Yes")
        exit()

print("No")
