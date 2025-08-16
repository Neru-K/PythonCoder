N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dict = {}

for i in range(M):
    if B[i] in dict:
        dict[B[i]] += 1

    else:
        dict[B[i]] = 1


ans = []

for j in range(N):
    if A[j] in dict and dict[A[j]] > 0:
        dict[A[j]] -= 1
    else:
        ans.append(str(A[j]))

print(*ans, sep=" ")
