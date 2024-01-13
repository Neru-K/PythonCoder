N, M = map(int, input().split())

result = "Yes"
B = [list(map(int, input().split()))]

for i in range(M - 1):
    if B[0][i + 1] - B[0][i] != 1:
        result = "No"

    elif B[0][i] % 7 == 0:
        result = "No"


for c in range(M):
    if result == "No":
        break

    for r in range(1, N):
        if c == 0:
            B.append(list(map(int, input().split())))

        if B[r][c] - B[r - 1][c] != 7:
            result = "No"
            break

print(result)
