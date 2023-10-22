H, W = map(int, input().split())

censors = []

S = [input() for _ in range(H)]

count = 0

for i in range(H):
    for j in range(W):
        flag = False

        if S[i][j] == ".":
            continue

        clearCount = 0
        for x in range(-1, 2):
            for y in range(-1, 1):
                if x >= 0 and y >= 0:  # それ自身はスキップ
                    clearCount += 1
                    continue
                if i + y < 0 or j + x < 0:  # 枠外はスキップ（上・左方向）
                    clearCount += 1
                    continue
                if i + y > H - 1 or j + x > W - 1:  # 枠外はスキップ（右・下方向）
                    clearCount += 1
                    continue
                if S[i + y][j + x] == "#":
                    flag = True
                    break

                if clearCount == 0:
                    count += 1
                flag = True
                break

            if flag:
                break

        if flag:
            continue

print(count)
