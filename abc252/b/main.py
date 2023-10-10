N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx = max(A)
result = "No"

for i in range(K):
    if A[B[i] - 1] == mx:
        result = "Yes"
        break

print(result)
