N, S, K = map(int, input().split())

price = 0

for i in range(N):
    P, Q = map(int, input().split())

    price += P * Q

if price < S:
    price += K

print(price)
