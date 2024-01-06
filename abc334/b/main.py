A, M, L, R = map(int, input().split())

if A > L and A < R:
    print((A - L // M) + (R - A // M))
else:
    print(R - L // M)
