N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()


C = A + B
C.sort()

dict = {}

for i in range(N + M):
    dict[C[i]] = i

for i in range(N - 1):
    if A[i] in dict and A[i + 1] in dict:
        #print(dict[A[i]])
        #print(dict[A[i + 1]])
        if dict[A[i]] + 1 == dict[A[i + 1]]:
            print("Yes")
            exit() 

print("No")