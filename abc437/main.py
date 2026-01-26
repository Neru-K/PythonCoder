T = int(input())
for i in range(T):
    N = int(input())
    diff = 0
    ans = 0
    sumwp = []

    for j in range(N):
        W, P = map(int, input().split())
        diff += P
        sumwp.append(W + P)

    sumwp.sort()

    for k in range(N):
        diff -= sumwp[k]
        if diff < 0:
            ans = k
            break

    print(ans)
