N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort()
price = 0

for i in range(0, N, D):
    last_d = sum(F[max(N - i - D, 0) : N - i])
    if last_d > P:
        price += P
    else:
        price += last_d

print(price)
