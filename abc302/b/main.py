H, W = map(int,input().split())
S = [input() for _ in range(H)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

y, x = 0, 0

for h in range(H):
    y = h
    for w in range(W):
        x = w

        if S[y][x] != 's':
            continue

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < W and 0 <= ny < H:

                if S[ny][nx] == 'n':
                    xdir = nx - x
                    ydir = ny - y

                    if nx + (xdir * 3) < 0 or nx + (xdir * 3) > W - 1:
                        continue
                    elif ny + (ydir * 3) < 0 or ny + (ydir * 3) > H - 1:
                        continue

                    xpos = [nx + (xdir * 1), nx + (xdir * 2), nx + (xdir * 3)]
                    ypos = [ny + (ydir * 1), ny + (ydir * 2), ny + (ydir * 3)]

                    if S[ypos[0]][xpos[0]] == 'u' and S[ypos[1]][xpos[1]] == 'k' and S[ypos[2]][xpos[2]] == 'e':
                        print(str(y + 1) + ' ' + str(x + 1))
                        print(str(ny + 1) + ' ' + str(nx + 1))
                        print(str(ypos[0] + 1) + ' ' + str(xpos[0] + 1))
                        print(str(ypos[1] + 1) + ' ' + str(xpos[1] + 1))
                        print(str(ypos[2] + 1) + ' ' + str(xpos[2] + 1))
                        exit()
