N, K, A = map(int, input().split())

result = (A + K - 1) % N

if result == 0:
    print(N)
else:
    print(result)
