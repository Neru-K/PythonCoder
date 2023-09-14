N, M = map(int, input().split())  # 一行目の入力を受け取り

matrix = [[0] * N for _ in range(N)]  # N x Nのマスを用意

for m in range(M):
    # 二行目の入力を受け取り
    row = list(map(int, input().split()))

    # 受け取った値をkとxに分割
    k = row[0]
    x = row[1:]

    for i in range(0, k):  # N!回ループさせる
        for j in range(i + 1, k):
            p1 = x[i] - 1
            p2 = x[j] - 1
            matrix[p1][p1] = 1  # 同じ人同士
            matrix[p1][p2] = 1  # 横のマス
            matrix[p2][p1] = 1  # 縦のマス

result = "Yes"

# 埋めたマスをチェック
for n in range(N):
    # ひとつでも0が見つかればNo
    if 0 in matrix[n]:
        result = "No"
        break

print(result)
