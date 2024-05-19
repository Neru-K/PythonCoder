N = int(input())
A = []

max_a = 0
for i in range(N):
    A.append(input())
    for j in range(N):
        if int(A[i][j]) > max_a:
            max_a = int(A[i][j])

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

result = []


def grid(y, x):
    
    for i in range(8):
        num = ""
        for j in range(N):
            nx = (x + (dx[i] * j)) % N
            ny = (y + (dy[i] * j)) % N

            num += A[ny][nx]

        result.append(num)


max_a = str(max_a)

for y in range(N):
    for x in range(N):
        if A[y][x] == max_a:
            grid(y, x)

result.sort(reverse=True)

print(result[0])