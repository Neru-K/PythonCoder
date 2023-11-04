from itertools import product

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for p in product((0, 1), repeat=N):
    flag = True
    for i in range(M):
        if p[A[i] - 1] == p[B[i] - 1]:
            flag = False
            break
    if flag:
        print("Yes")
        exit()

print("No")
