N, K, A = map(int, input().split())

amari = K % N

if N == 1:
    print(N)
else:
    print(N - A + amari)
