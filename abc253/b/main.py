H, W = map(int, input().split())

S = [input() for _ in range(H)]

v1 = 0
v2 = 0
h1 = 0
h2 = 0
count = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            if count == 0:
                v1 = i
                h1 = j
                count += 1
            elif count == 1:
                v2 = i
                h2 = j

print(abs(v2 - v1) + abs(h2 - h1))
