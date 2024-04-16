N = int(input())
S = list(map(int,input().split()))

result = [S[0]]

for i in range(N - 1):
    result.append(S[i + 1] - S[i])

print(*result)