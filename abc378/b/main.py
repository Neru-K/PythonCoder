N = int(input())


dict = {}

for i in range(N):
    q,r = map(int, input().split())
    dict[i] = (q, r)

Q = int(input())

for j in range(Q):
    t, d = map(int, input().split())
    q, r = dict[t-1]
    
    print((d % q) // r)