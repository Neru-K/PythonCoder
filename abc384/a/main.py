N, c1, c2 = map(str, input().split())

S = input()

ans = ""

for i in range(int(N)):
    if S[i] != c1:
        ans += c2
    else:
        ans += S[i]

print(ans)