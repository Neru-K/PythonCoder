N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)

result = 1

if A[-1] == 0:
    print(0)
    exit()

for i in range(N):
    result *= A[i]

    if result > 1000000000000000000:
        print(-1)
        exit()

print(result)