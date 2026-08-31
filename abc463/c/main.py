N = int(input())

HL = []

for _ in range(N):
    H, L = map(int, input().split())
    HL.append([H, L])

Q = int(input())
T = list(map(int, input().split()))
TJ = []

for j in range(Q):
    TJ.append([T[j], j])

TJ.sort(reverse=True)

mx = 0

ans = [0] * Q

for t, j in TJ:
    while HL and HL[-1][1] > t:
        h, l = HL.pop()
        if h > mx:
            mx = h

    ans[j] = mx

for a in ans:
    print(a)
