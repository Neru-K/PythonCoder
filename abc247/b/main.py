N = int(input())
st = [list(map(str, input().split())) for _ in range(N)]

result = "Yes"

for i in range(N):
    count = 0
    for j in range(i, N):
        if i != j:
            if (st[i][0] != st[j][0] or st[i][0] != st[j][1]) or (
                st[i][1] != st[j][0] or st[i][1] != st[j][1]
            ):
                count += 1
                break


print(result)
