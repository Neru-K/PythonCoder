N, M = map(int, input().split())

visited = set()


def search_grid(y, x, visited, n=N):

    # 上下左右ななめ8方向への移動を表す配列
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [-2, -2, -1, 1, 2, 2, 1, -1]

    # 上下左右の移動をループで処理
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # ここで、nxとnyは移動先の座標を表します
        # 移動先が迷路の範囲内であるか、壁でないかなどのチェックを行う
        if 0 <= nx < n and 0 <= ny < n:
            # 移動可能な場合の処理をここに書く
            visited.add((ny, nx))


for i in range(M):
    a, b = map(int, input().split())
    search_grid(a-1, b-1, visited)
    visited.add((a-1, b-1))


print(N * N - len(visited))