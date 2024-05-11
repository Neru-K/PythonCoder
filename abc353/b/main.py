#N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
N, K = map(int, input().split())
A = list(map(int, input().split()))
#N, M = map(int, input().split())
#A = [list(map(int, input().split())) for _ in range(N)]

s = [0]

for i in range(N):
    if s[len(s) - 1] + A[i] <= K:
        s[len(s) - 1] += A[i]
    else:
        s.append(A[i])

print(len(s))