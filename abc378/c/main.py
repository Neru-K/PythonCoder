N = int(input())
A  = list(map(int, input().split()))

dict = {}

for i in range(N):
    if A[i] in dict:
        print(dict[A[i]])
    else:
        print(-1)
    
    dict[A[i]] = (i + 1)