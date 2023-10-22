N = int(input())

h = [0] * 24
count = 0

for i in range(N):
    W, X = map(int, input().split())
    for j in range(9 + X, 18 + X):
        h[j % 24] += W

print(max(h))
