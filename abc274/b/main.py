H, W = map(int, input().split())
C = [input() for _ in range(H)]

result = []

for c in range(W):
    count = 0
    for r in range(H):
        if C[r][c] == "#":
            count += 1

    result.append(str(count))

print(" ".join(result))
