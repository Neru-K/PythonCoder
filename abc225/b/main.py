N = int(input())
array = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int,input().split())
    array[a - 1].append(b - 1)
    array[b - 1].append(a - 1)

for i in range(N):
    if len(array[i]) == N - 1:
        print("Yes")
        exit()

print("No")