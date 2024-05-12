H, W = map(int, input().split())

A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

if A == B:
    print("Yes")
    exit()

for i in range(1, H):
    Acopy = A.copy()
    for j in range(W):
        
