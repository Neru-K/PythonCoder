N = int(input())
A = list(map(int,input().split()))

B = []

for i in range(0,N - 1):
    B.append(A[i] * A[i + 1])

print(*B)