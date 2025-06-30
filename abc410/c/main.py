N, Q = map(int, input().split())
A = [i for i in range(1, N + 1)]

offset = 0

for _ in range(Q):
    q, *rest = list(map(int, input().split()))
    if q == 1:
        # Apをxに変更する
        p, x = rest
        A[(p - 1 + offset) % N] = x
    elif q == 2:
        # Apを出力する
        p = rest[0]
        print(A[(p - 1 + offset) % N])
    else:
        # Aの先頭を末尾にする操作をk回繰り返す
        k = rest[0]
        offset += k
