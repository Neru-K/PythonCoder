H, W = map(int, input().split())
A = []
B = []

for h in range(H * 2):
    if h < H:
        A.append(list(map(int, input().split())).sort())
    else:
        B.append(list(map(int, input().split())).sort())
