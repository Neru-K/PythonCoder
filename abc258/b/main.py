N = int(input())
start = []
A = []

max_a = 0
for i in range(N):
    A.append(input())
    for j in range(N):
        if A[j] > max_a:
            max_a = A[j]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

visited = set()
max_result = ""


def grid(y, x):
    max = 0
    max_ny = 0
    max_nx = 0
    
    for i in range(8):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % N

        if not (ny, nx) in visited:
            visited.add((ny, nx))
            if A[ny][nx] > max:
                max = A[ny][nx]
                max_ny = ny
                max_nx = nx

    return (max_ny, max_nx)


returned_tuple = (0, 0)

for y in range(N):
    for x in range(N):
        if A[y][x] == max_a:
            returned_tuple = grid(y, x)