N, M = map(int, input().split())
increase = [0] * (N + 1)
decrease = [0] * (N + 1)

for _ in range(M):
    L, R = map(int, input().split())
    increase[L - 1] += 1
    decrease[R] += 1

min = INF = 1 << 60
count = 0

for i in range(N):
    count += increase[i]
    count -= decrease[i]

    if count < min:
        min = count

print(min)
