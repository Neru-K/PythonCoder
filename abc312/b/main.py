#B - TaK Code

""" 
テスト2
・まず3つ連続して#のところ以外は考えなくていい
・制約は割と緩め
・まずは愚直に実装してみよう
・愚直に実装するならどういう流れになるか？
・まず先に入力を読み込んじゃう？
・実装面倒くさそう・・・
・ループしながら他のマスと比較していく系のやつ苦手意識がある
・行の流れ　3つ続いているますがあるかどうか？
・あったらどうする？
・次の行と比較

解説を見た後

・左上が定ったら、あとは条件分岐で確認するだけ
・愚直な実装をするので合っていたが実装をするのをなぜ諦めるのか
・開発だとコード書くの大好きなのに競プロだと実装めんどくさく感じてしまうのはなぜ？
・困難は分割せよ。少しずつ分割する。
・関数をもっと作るといいかもしれない。いつも開発でやっているように
・少しずつの部分部分なら実装していけるかも。細かく部品を分ける感じで。頭の整理にもなる
・基本関数を書く、くらいに思っておこうか

ACとったあと
・実装にめっちゃ苦労した・・・
・どこをミスっていたか？
・関数のreturnのインデントを間違えていた
・各グリッドのセルの比較を間違えていた。添字を。
・間違えるのはいい。効率のいいデバッグ方法を身につけなければ。
・競プロデバッグ完全ガイドとかあったら面白そう
・上位ランカーがどのようにデバッグしているか、コードを辿ったらわかるかも
https://qiita.com/amaguri0408/items/61d65c3bea3a5815d704
https://qiita.com/lanevok/items/bbdf5a4f642d027a5d4e
"""

def isTakCode(r, c, grid):

    if r + 8 > N or c + 8 > M:
        return False
    elif grid[r][c] == "#":
        lu = [
            ["#", "#", "#", "."],
            ["#", "#", "#", "."],
            ["#", "#", "#", "."],
            [".", ".", ".", "."]
        ]
        for i in range(16):
            x = i % 4
            y = i // 4
            if grid[r + y][c + x] != lu[y][x]:
                return False

        ru = [
            [".", ".", ".", "."],
            [".", "#", "#", "#"],
            [".", "#", "#", "#"],
            [".", "#", "#", "#"]
        ]

        for j in range(16):
            x = j % 4
            y = j // 4
            if grid[r + 5 + y][c + 5 + x] != ru[y][x]:
                return False
            
        return True


N,M = map(int,input().split())

grid = []
count = 0
result = []

for i in range(N):
    S = input()
    grid.append(S)

for i in range(N):
    for j in range(M):
        if isTakCode(i,j,grid):
            result.append(str(i + 1) + " " + str(j + 1))

print("\n".join(result))
