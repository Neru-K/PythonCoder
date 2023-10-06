R, C = map(int, input().split())

num = 0

for i in range(1, 16):
    num += 1
    for j in range(1, 16):
        num += 1
        if i == R and j == C:
            break
