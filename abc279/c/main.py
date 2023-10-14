H, W = map(int, input().split())

result = "Yes"

S = [input() for _ in range(H)]
S.sort()

T = [input() for _ in range(H)]
T.sort()

for i in range(H):
    if S[i] != T[i]:
        result = "No"
        break

print(result)
