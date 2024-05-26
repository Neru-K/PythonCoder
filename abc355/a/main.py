#N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
A, B = map(int, input().split())
#list_s = list(map(int, input().split()))
#N, M = map(int, input().split())
#A = [list(map(int, input().split())) for _ in range(N)]

lst = list(set([A,B]))

if len(lst) < 2:
    print(-1)
else:
    print(6 - (A + B))