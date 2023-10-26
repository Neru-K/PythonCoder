N, M = map(int, input().split())

power = [0] * N

for i in range(M):
    A, B = map(int, input().split())
    power[B - 1] += 1

if power.count(0) == 1:
    index_of_zero = power.index(0)
    print(index_of_zero + 1)
else:
    print(-1)
