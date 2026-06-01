S = list(input())
T = list(input())
X = []

for i in range(len(S)):
    s = S[i]
    t = T[i]
    if ord(s) > ord(t):
        S[i] = t
        X.append("".join(S))

for j in range(len(S) - 1, -1, -1):
    s = S[j]
    t = T[j]
    if ord(s) < ord(t):
        S[j] = t

        X.append("".join(S))

print(len(X))

for x in X:
    print(x)
