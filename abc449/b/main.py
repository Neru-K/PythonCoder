H, W, Q = map(int, input().split())

for _ in range(Q):
    n, d = map(int, input().split())

    if n == 1:
        H = H - d
        print(d * W)
    else:
        W = W - d
        print(d * H)
