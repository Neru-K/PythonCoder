from collections import deque

# 上下左右への移動を表す配列
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 迷路の例（0: 通路, 1: 壁）
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

# スタート地点とゴール地点
start = (0, 0) # (行, 列)
goal = (3, 4)

# 訪問済み座標を記録するセット
visited = set()

# 幅優先探索用のキュー
queue = deque([start])

# 訪問済みに追加
visited.add(start)

while queue:
    y, x = queue.popleft()
    
    # ゴールに到達した場合の処理
    if (y, x) == goal:
        print("ゴールに到達しました！")
        break
    
    # 上下左右の移動をループで処理
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 移動先が迷路の範囲内かつ未訪問であるかのチェック
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and (ny, nx) not in visited:
            queue.append((ny, nx))
            visited.add((ny, nx))

# 訪問済み座標の出力（デバッグ用）
print(visited)
