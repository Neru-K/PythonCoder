#A + B + C = X
#A = X - B - C 
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))

BC = []
for i in range(M):
    for j in range(L):
        BC.append(B[i] + C[j])

st1 = set(BC)
st2 = set()

for i in range(N):
    for j in range(len(BC)):
        st2.add(A[i] + BC[j])

for i in range(Q):
    if X[i] in st2:
        print('Yes')
    else:
        print('No')