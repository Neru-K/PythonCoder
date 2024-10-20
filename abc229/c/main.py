N, W  = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: x[0], reverse=True)

sum = 0

for i in range(N):
    if lst[i][1] <= W:
        sum += (lst[i][0] * lst[i][1])
    else:
        sum += (lst[i][0] * W)

    W -= lst[i][1]

    if W <= 0:
        break

print(sum)