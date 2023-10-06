N = int(input())
ST = [list(map(str, input().split())) for _ in range(N)]

result = "No"

for i in range(N):
    flag = False

    for j in range(i + 1, N):
        if ST[i][0] == ST[j][0] and ST[i][1] == ST[j][1]:
            result = "Yes"
            flag = True
            break

    if flag:
        break

print(result)
