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

grid = [[''] * N for _ in range(N)]

print(grid)

A = [list(input()) for _ in range(N)]

print(A)

#middle
for i in range(1,N - 1):
    for j in range(1,N - 1):
        grid[i][j] = A[i][j]

print(grid)

outer = []

for i in range(N * 4 - 4):
    if i < N:
        print(i)
    elif i < N * 2 - 1:
        print(N - 1 + (i % 4 + 1) * N)
    elif i < N * 3 - 2:
        print(N * N - 1 - ((i + 2) % 4))
    else:
        print()

exit()
print(i % 4)