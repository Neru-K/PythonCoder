N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

prices = {}

for i in range(M):
    prices[D[i]] = P[i + 1]

result = 0

for i in range(N):
    if C[i] in prices:
        result += prices[C[i]]
    else:
        result += P[0]

print(result)
