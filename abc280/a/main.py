H, W = map(int, input().split())

S = [input() for _ in range(H)]

count = 0

for i in range(H):
    count += S[i].count("#")

print(count)
