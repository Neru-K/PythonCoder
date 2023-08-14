N = int(input())

cnt = N - 1

for i in range(cnt - 1, 0, -1):
    cnt *= i

print(cnt)
