N, Q = map(int, input().split())

L = 0
R = 1
count = 0

def calcDistance(N, S, E, X):
    if S > E:
        S, E = E, S

    if S < X and X < E:
        return N - (E - S)
    else:
        return E - S

for i in range(Q):
    H, T = map(str, input().split())
    T = int(T) - 1

    if H == "R":
        count += calcDistance(N, R, T, L)
        R = T

    else:
        count += calcDistance(N, L, T, R)
        L = T

print(count)