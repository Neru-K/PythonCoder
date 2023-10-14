N = int(input())
A = list(map(int, input().split()))

result = "YES"
for i in range(N):
    for j in range(i + 1, N):
        if A[i] == A[j]:
            result = "NO"
            break
print(result)
