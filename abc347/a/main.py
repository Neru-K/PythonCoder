N, K = map(int,input().split())
A = list(map(int,input().split()))

result = []

for a in A:
    if a % K == 0:
        result.append(a // K)

print(*result)