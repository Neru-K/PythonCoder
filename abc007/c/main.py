from collections import deque

# 入力
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input() for _ in range(R)]

""" 
edgesを
[
[1,2],
[3,4],
[4]
]

みたいな形にする
"""

def fourDirection(sy, sx):
	# 上下左右への移動を表す配列
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]

	# ここで、(y, x)は現在位置を表します
	y, x = sy, sx  # 例えば、グリッドの開始位置など

	# 上下左右の移動をループで処理
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		# ここで、nxとnyは移動先の座標を表します
		# 移動先が迷路の範囲内であるか、壁でないかなどのチェックを行う
		if 0 <= nx < C and 0 <= ny < R and maze[ny][nx] != "#":
			# 移動可能な場合の処理をここに書く
			print("移動先:", nx, ny)


exit()






# 隣接リストの作成
G = [ list() for _ in range(R * C) ]
for a, b in edges:
	G[a].append(b)
	G[b].append(a)

# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
dist = [ -1 ] * (N + 1)
dist[1] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while len(Q) >= 1:
	pos = Q.popleft() # キュー Q の先頭要素を取り除き、その値を pos に代入する
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)

# 頂点 1 から各頂点までの最短距離を出力
for i in range(1, N + 1):
	print(dist[i])