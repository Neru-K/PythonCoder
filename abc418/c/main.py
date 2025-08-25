N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 累積和を作っておく

A.sort()

def binary_search(num):
  L, R = 0, N
  
  while R > L + 1:
    M = (L + R) // 2
    if A[M] > num:
      R = M
    else:
      L = M
    
  return L
  

for i in range(Q):
    ans = 0
    B = int(input())

    ### ここのループの処理をどう効率化するか
    for j in range(N):
        # ans += min(A[j], B - 1)
        # small と bigの境目を二分探索で出しておき、前半の和を累積和から引き当てる。
        # 後半は、残りの要素数を掛け算して出す。
        

    print(ans + 1)
