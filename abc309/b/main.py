import copy

N = int(input())

A = [list(input()) for _ in range(N)]

grid = copy.deepcopy(A)

#top
for i in range(N - 1):
    grid[0][i + 1] = A[0][i]

#right
for i in range(N - 1):
    grid[i + 1][N - 1] = A[i][N - 1]

#bottom
for i in range(1, N):
    grid[N - 1][i - 1] = A[N - 1][i]

#left
for i in range(1, N):
    grid[i - 1][0] = A[i][0]

s = ''

for i in range(N):
    line = ''.join(grid[i])
    s += line
    if i < N - 1:
        s += '\n'

print(s)