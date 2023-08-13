n, m, t = map(int, input().split())  # n 容量 m カフェ回数 t 帰宅時間

ab = [list(map(int, input().split())) for _ in range(m)]

charge = n
spent = 0
result = "Yes"

for i in range(m):
    if i == 0:
        charge -= ab[i][0]
    else:
        charge -= ab[i][0] - ab[i - 1][1]

    if charge <= 0:
        result = "No"
        break
    charge += ab[i][1] - ab[i][0]
    if charge > n:
        charge = n

charge -= t - ab[len(ab) - 1][1]
if charge <= 0:
    result = "No"

print(result)
