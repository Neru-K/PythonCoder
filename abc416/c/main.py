N, K, X = map(int, input().split())

list_S = []

for _ in range(N):
    S = input()
    list_S.append(S)

now = [""]
next = []

for k in range(K):
    for nw in now:
        for s in list_S:
            next.append(nw + s)

    now = next
    next = []

now.sort()
print(now[X - 1])
