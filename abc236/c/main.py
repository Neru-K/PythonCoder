N, M = map(int, input().split())

S = list(map(str, input().split()))
T = list(map(str, input().split()))

set = set()

for i in range(M):
    set.add(T[i])

for j in range(N):
    if S[j] in set:
        print("Yes")
    else:
        print("No")
