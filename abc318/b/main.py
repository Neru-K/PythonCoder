# B - Overlapping sheets

##解法 グリッドを用意して塗りつぶす

"""
100*100の白いマス目があると考えて、各シートを順番にループさせてそのマス目を塗りつぶしていく。
その後塗り潰された箇所をカウント。

1. 100*100のグリッドを用意する。
2. 各シートごとにループし、シートの面積に該当するグリッドに数字を足していく。
3｡ 2が終わったら、グリッドのマス目を順番にループして2以上の数字であるマス目を数える。

※2次元累積和、2次元いもす法、セグツリーといった解法もあるらしい（B問題ではオーバーキルっぽい）
"""

N = int(input())

grid = [[0] * 100 for _ in range(100)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    for j in range(A, B):
        for k in range(C, D):
            grid[j][k] = True

count = 0

for i in range(100):
    for j in range(100):
        if grid[i][j]:
            count += 1

print(count)
