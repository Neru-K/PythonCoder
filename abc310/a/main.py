N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

min = min(D)

if P > Q + min:
    print(Q + min)
else:
    print(P)
