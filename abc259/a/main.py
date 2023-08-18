N, M, X, T, D = map(int, input().split())  # X歳からN際まで変化なし N歳の時Tcm　毎年D伸びたß

if M >= X:
    print(T)
elif M == 0:
    print(T - (X * D))
else:
    print(T - D * (X - M))
