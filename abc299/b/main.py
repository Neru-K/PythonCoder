N, T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

mx = [-1,-1] #i,v
mx2 = [-1,-1]
count = 0

for i in range(N):
    if C[i] == T:
        if R[i] > mx[1]:
            mx[0] = i
            mx[1] = R[i]

    if C[i] == C[0]:
        if R[i] > mx2[1]:
            mx2[0] = i
            mx2[1] = R[i]

if mx[0] > -1:
    print(mx[0] + 1)
else:
    print(mx2[0] + 1)