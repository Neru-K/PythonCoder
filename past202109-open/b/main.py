N, M = map(int,input().split())
A = list(set(list(map(int,input().split()))))
B = set(list(map(int,input().split())))

result = []

for i in range(N):
    if A[i] in B:
        result.append(A[i])

result.sort()

print(*result)