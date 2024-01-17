N = int(input())

A = [list(map(int, input().split())) for _ in range(2)]

upper = [A[0][0]]
lower = [A[1][0]]
uppersum = A[0][0]
lowersum = A[1][0]

result = 0

for i in range(1, N):
    upper.append(A[0][i] + upper[i - 1])
    uppersum += A[0][i]
    lower.append(A[1][i] + lower[i - 1])
    lowersum += A[1][i]

for i in range(N):
    """print(uppersum - upper[i])
    print(lowersum - lower[i])"""
    upremain = uppersum - upper[i] + A[0][len(lower) - 1]
    lowremain = lowersum - lower[i] + A[1][i]

    if upremain < lowremain:
        result = upper[i] + lowremain
        # print(lowremain)
        break

if result == 0:
    result = sum(A[0]) + A[1][N - 1]
print(result)
