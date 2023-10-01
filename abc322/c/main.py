N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0

for i in range(1, N + 1):
    if i == A[count]:
        print(0)
        count += 1
    else:
        print(A[count] - i)
