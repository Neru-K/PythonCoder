N = int(input())

A = list(map(int, input().split()))

B = []

for i in range(N):
    B.append([A[i],i])

B.sort(key=lambda x:x[0])

print(B)