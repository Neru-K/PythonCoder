N, Q = map(int, input().split())
A = list(map(int, input().split()))


for i in range(Q):
    ans = 0
    B = int(input())

    ### ここのループの処理をどう効率化するか
    for j in range(N):
        ans += min(A[j], B - 1)

    print(ans + 1)
