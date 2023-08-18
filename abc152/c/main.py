N = int(input())
P = list(map(int, input().split()))

count = 0
min = P[0]

for i in range(N):
    if P[i] <= min:
        count += 1

    if min > P[i]:
        min = P[i]

print(count)
