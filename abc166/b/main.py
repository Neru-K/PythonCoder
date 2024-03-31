N, K = map(int,input().split())
array = [0] * N

for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for j in range(d):
        array[A[j] - 1] += 1


count = 0

for i in range(N):
    if array[i] == 0:
        count += 1

print(count)