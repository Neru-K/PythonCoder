Q = int(input())

A = []

for i in range(Q):
    q,n = map(int,input().split())
    if q == 1:
        A.append(n)
    else:
        print(A[len(A) - n])