N = int(input())

lr = [list(map(int, input().split())) for _ in range(N)]

sum = 0

for i in range(N):
    sum += lr[i][1] - lr[i][0] + 1

print(sum)
