N, M = map(int, input().split())

result = "No"
P,C,L = [],[],[]

for i in range(N):
    splitted = list(map(int, input().split()))

    P.append(splitted[0])
    C.append(splitted[1])
    L.append(set(list(splitted[2:])))


for i in range(N):
    for j in range(N):
        if P[i] >= P[j] and L[i] <= L[j] and (P[i] > P[j] or len(L[i]) < len(L[j])):
            print("Yes")
            exit()

print("No")
