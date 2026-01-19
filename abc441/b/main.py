N, M = map(int, input().split())
S = list(input())
T = list(input())
Q = int(input())

for i in range(Q):
    w = input()
    isTakahashi = True
    isAoki = True
    for c in w:
        if c not in S:
            isTakahashi = False
            break

    for ch in w:
        if ch not in T:
            isAoki = False
            break

    if isTakahashi and isAoki:
        print("Unknown")
    elif isTakahashi:
        print("Takahashi")
    else:
        print("Aoki")
