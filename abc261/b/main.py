n = int(input())

a = [input() for _ in range(n)]

result = "correct"

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if a[i][j] == "W" and a[j][i] == "W":
            result = "incorrect"
            break
        elif a[i][j] == "L" and a[j][i] == "L":
            result = "incorrect"
            break
        elif a[i][j] == "D" and a[j][i] != "D":
            result = "incorrect"
            break
        elif a[i][j] != "D" and a[j][i] == "D":
            result = "incorrect"
            break

print(result)
