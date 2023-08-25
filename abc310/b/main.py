N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

result = "No"

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        flag = False

        if P[i][0] >= P[j][0]:
            nums = P[i][2:]

            for k in range(2, len(P[j])):
                if P[j][k] not in nums:
                    flag = True
                    break

        if flag:
            break

        if P[i][0] > P[j][0] or len(P[i]) < len(P[j]):
            result = "Yes"
            break

print(result)
