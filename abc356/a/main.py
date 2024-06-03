#N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
N, L, R = map(int, input().split())
#list_s = list(map(int, input().split()))
#N, M = map(int, input().split())
#A = [list(map(int, input().split())) for _ in range(N)]
A  = []

for i in range(1,N+1):
    A.append(i)

l = A[0:L-1]
m = A[L-1:R]
m.reverse()
r = A[R:]
print(*(l+m+r))