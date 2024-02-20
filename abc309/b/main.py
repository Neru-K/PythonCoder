"""
・どういう方向性でやるか？
・制約が小さいので、ループを回すのを上手に実装するだけか
・時計回りにリストに格納したい
・まずは一行目
・一番下は文字列をリバースすればいいだけでは？
・TRDLに別々でリストに格納する。
・各辺をN-1個ずつに格納し、ずらす。
"""

N = int(input())
A = [input() for _ in range(N)]
p = []

p.append(A[0][0:N - 1])

right = ""
for i in range(N - 1):
    right += A[i][N - 1]

p.append(right)

print(A[N - 1])

p.append(A[N - 1][1:N][::-1])

left = ""
for i in range(0,N-1):
    left += A[i][0]

p.append(left)

grid = A.copy()

print(p[3])

grid[0] = p[0] + p[3][N - 2]

print(grid)