N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
#A, B = map(int, input().split())
H = list(map(int, input().split()))
#N, M = map(int, input().split())
#A = [list(map(int, input().split())) for _ in range(N)]

l = H[0]

for i in range(1,N):
    if H[i] > l:
        print(i + 1)
        exit()

print("-1")