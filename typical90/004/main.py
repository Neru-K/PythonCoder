# https://drken1215.hatenablog.com/entry/2021/07/25/215000

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

col = [0] * W
row = [0] * H

for i in range(H):
    for j in range(W):
        col[j] += A[i][j]
        row[i] += A[i][j]


for k in range(H):
    arr = []
    for l in range(W):
        arr.append(str(row[k] + col[l] - A[k][l]))

    print(" ".join(arr))


""" 解答例

 # 入力
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 前処理
yoko = list(map(sum, A))
tate = list(map(sum, zip(*A)))

# 各マス
for i in range(H):
    print(" ".join(map(lambda j: str(yoko[i] + tate[j] - A[i][j]), range(W)))) """
