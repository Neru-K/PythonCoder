N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 累積和を作っておく
ruisekiwa = [0]

for n in range(N):
    ruisekiwa.append(ruisekiwa[-1] + A[n])


def binary_search(num):
    L, R = -1, N

    while R > L + 1:
        M = (L + R) // 2
        if A[M] >= num:
            R = M
        else:
            L = M

    return L


for i in range(Q):
    ans = 0
    B = int(input())

    ### ここのループの処理をどう効率化するか
    # for j in range(N):
    #   ans += min(A[j], B - 1)

    if A[-1] < B:
        print(-1)
        continue

    # small と bigの境目を二分探索で出しておき、前半の和を累積和から引き当てる。
    # 後半は、残りの要素数を掛け算して出す。
    idx = binary_search(B)
    before = ruisekiwa[idx + 1]
    after = (N - (idx + 1)) * (B - 1)

    print(before + after + 1)
