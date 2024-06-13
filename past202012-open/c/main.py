N = int(input())
S = list(input())

for i in range(N):
    c = S[i]
    for j in range(N):
        if S[j] == c:
            S[j] = ''

    S.append(c)