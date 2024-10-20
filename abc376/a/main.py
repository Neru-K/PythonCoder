N, C = map(int, input().split())
T = list(map(int, input().split()))

count = 1
gottime = T[0]

for i in range(1, N):
    if T[i] - gottime >= C:
        count += 1
        gottime = T[i]

print(count)