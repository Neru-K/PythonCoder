#N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
N,M = map(int, input().split())
A = list(map(int, input().split()))
#N, M = map(int, input().split())
nut = [0] * M

for i in range(N):
    X = list(map(int, input().split()))
    for j in range(M):
        nut[j] += X[j]

for k in range(M):
    if nut[k] < A[k]:
        print("No")
        exit()

print("Yes")