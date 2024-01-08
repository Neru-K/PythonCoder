# C - Rotate Colored Subsequence

##解法 同じ色同士でまとめてからrotate

"""
各色ごとに処理を分けて愚直に実装すると、M(色)×N(文字列の長さ)となり、計算量O(MN)のTLEとなる。
そこで計算量を減らす工夫が必要になる。

・まずは文字列Sを一回走査して、各色に対しての文字の位置を格納するリストpsを作る *Point1
・暫定的にN個の文字列のリストを用意しておき、後から文字を差し替えていく *Point2
・ループの際に(i - 1) % 3 , (i + 1) % 3等とすることで、左右にシフトすることができる *Point3
"""
N, M = map(int, input().split())  # N 文字の長さ　M 色の数
S = input()
C = list(map(int, input().split()))

# Point1 各色の文字位置を格納する変数
ps = [[] for _ in range(M)]

# Cをループして、各色が文字列Sのそれぞれどの位置にあるかを格納
for i, c in enumerate(C):
    ps[c - 1].append(i)

# Point2　暫定的に、N個の文字列のリストを用意
result = [""] * N

for i in range(len(ps)):
    k = len(ps[i])
    for j in range(k):
        idx = ps[i][j]
        # Point3 新しい文字の位置を計算
        newchar = S[ps[i][(j - 1) % k]]
        result[idx] = newchar

print("".join(result))
