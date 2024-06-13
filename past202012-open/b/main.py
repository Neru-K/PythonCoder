N = int(input())
S = list(input())
T = ''

for i in range(N):
    c = S[i]
    T = list(T)
    for j in range(len(T)):
        if T[j] == c:
            T[j] = ''

    T.append(c)
    T = "".join(T)

print(T)