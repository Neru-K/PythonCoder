from itertools import product

N, W = map(int, input().split())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0

for pro in product((0, 1), repeat=N):
    o = 0
    t = 0
    for i, c in enumerate(pro):
        if c == 1:
            o += A[i]
            t += B[i]

    if t <= W and o > ans:
        ans = o

print(ans)
