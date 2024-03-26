N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)

div = X // sumA

count = N * div

total = sumA * div

for i in range(N):
    total += A[i]
    count += 1
    if total > X:
        break

print(count)