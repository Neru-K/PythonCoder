N, X = map(int, input().split())
S = list(map(int, input().split()))
sum = 0

for i in range(N):
    if S[i] <= X:
        sum += S[i]

print(sum)
