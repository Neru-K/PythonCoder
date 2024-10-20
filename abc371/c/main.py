N = int(input()) #頂点

MG = int(input()) #Gの辺の数
G = set()

for i in range(MG):
    u,v = map(int,input().split())
    G.add((u,v))

MH = int(input())
H = set()

for j in range(MH):
    a,b = map(int, input().split())
    H.add((a,b))

A = [list(map(int, input().split())) for _ in range(N - 1)]

price = 0

for k in range(N-1):
    for l in range(k+1, N):

        m = (k + 1, l + 1)
        if (m in G and m in H) or (m not in G and m not in H):
            pass
        else:
            price += A[k][l - (k + 1)]


print(price)