N = int(input())
D = list(map(int,input().split()))

sorted = sorted(D)

count = 0

if N % 2 == 0:
    start = sorted[(N-1)//2]+1
    end = sorted[(N+1)//2]+1
    for i in range(start,end):
        count += 1

print(count)