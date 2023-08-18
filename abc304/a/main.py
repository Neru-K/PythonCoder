N = int(input())
S = []
A = []

min = 1000000001
startpos = 0

for i in range(N):
    s, a = map(str, input().split())
    S.append(s)
    if int(a) < min:
        startpos = i
        min = int(a)

S += S

for j in range(startpos, N + startpos):
    print(S[j])
