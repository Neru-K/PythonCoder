N = int(input())
A = list(map(int,input().split()))

result = []

for i in range(N-1):
    start = A[i]
    end = A[i + 1]
    result.append(A[i])
    if abs(start - end) > 1:
        step = 1
        if start > end:
            step = -1

        for j in range(start + step, end, step):
            result.append(j)

result.append(A[N - 1])

print(*result)